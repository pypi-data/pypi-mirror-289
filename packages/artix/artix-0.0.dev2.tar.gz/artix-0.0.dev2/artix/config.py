"""Module defining the configuration system for Artix."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

import loguru
import requests
import tomli


class Repository:
    """Represents a configured repository."""

    name: str
    source: str

    def __init__(self, *, name: str, source: str) -> None:
        """Initialize a repository with the given reference source string."""
        self.name = name
        self.source = source

    def __repr__(self) -> str:
        """Return a string representation of the repository."""
        return self.source

    def _resolve(self, version: dict[str, str]) -> str:
        """Return the full URL to pull the artifact from."""
        loguru.logger.info("determining full URL for {}", self)
        url = copy.copy(self.source)
        loguru.logger.debug("version information: {}", version)
        for key, value in version.items():
            loguru.logger.debug("replacing ${{{}}} with {}", key, value)
            url = url.replace(f"${{{key}}}", value)
        loguru.logger.info("full URL for artifact: {}", url)
        return url

    def pull(self, version: dict[str, str], destination: str | Path) -> None:
        """Pull a versioned copy of the artifact from the repository."""
        # Determine the full, proper URL of the source.
        url = self._resolve(version=version)

        destination = Path(destination).absolute()
        destination.parent.mkdir(parents=True, exist_ok=True)

        # Download the artifact to the intended destination.
        response = requests.get(url=url, timeout=300)

        with destination.open(mode="wb") as artifact:
            artifact.write(response.content)


class ArtifactNotOnDiskError(Exception):
    """Represents a case where the artifact is not on disk."""


class Artifact:
    """Represents a single managed artifact."""

    destination: Path
    locked: bool
    name: str
    repository: Repository
    version: dict[str, str]

    def __init__(
        self,
        *,
        destination: str | Path,
        locked: bool,
        name: str,
        repository: Repository,
        version: dict[str, str],
    ) -> None:
        """Initialize a managed artifact instance."""
        self.destination = Path(destination).absolute()
        self.locked = locked
        self.name = name
        self.repository = repository
        self.version = version

    def __repr__(self) -> str:  # pragma: no cover
        """Return a string representation of the managed artifact."""
        return self.name

    @property
    def sha256sum(self) -> str:
        """Return the SHA256 checksum of the downloaded artifact on disk."""
        if not self.destination.exists():  # pragma: no cover
            raise ArtifactNotOnDiskError
        with self.destination.open(mode="rb") as artifact_file:
            return hashlib.sha256(artifact_file.read()).hexdigest()

    def sync(self, expected: str | None = None) -> bool:
        """Pull the artifact."""
        # Ensure the artifact doesn't already exist on disk.
        if self.destination.exists() and expected is not None:
            loguru.logger.info(
                "artifact '{}' already exists on disk",
                self.name,
            )
            if self.sha256sum != expected:
                loguru.logger.error(
                    "'{}' does not match expected hash value!",
                    self.name,
                )
                loguru.logger.error("expected hash: {}", expected)
                loguru.logger.error("calculated hash: {}", self.sha256sum)
                return False
            return True

        loguru.logger.info("pulling '{}' to {}", self.name, self.destination)
        self.repository.pull(
            destination=self.destination,
            version=self.version,
        )
        return True


class Lockfile:
    """Represents a single Artix project lockfile."""

    _checksums: dict[str, str]
    _root: Path

    def __init__(self, root: Path) -> None:
        """Initialize a project's Artix lockfile."""
        self._root = root
        self._checksums = self.load()

    @property
    def root(self) -> Path:
        """Return the absolute path to the root of the project."""
        return self._root

    @property
    def path(self) -> Path:
        """Return the absolute path to the Artix lockfile."""
        return self.root / "artix.lock.json"

    def checksum(self, artifact: str) -> str:
        """Return the checksum of the artifact."""
        return self._checksums.get(artifact.name)

    def load(self) -> dict[str, str]:
        """Read in the Artix lockfile into the instance."""
        if not self.path.exists():
            loguru.logger.warning("{} not found", self.path)
            return {}

        with self.path.open(mode="r") as lockfile:
            return json.load(lockfile)

    def add(self, artifact: Artifact) -> None:
        """Add a single artifact to the lockfile and saves it."""
        self._checksums[artifact.name] = artifact.sha256sum
        self.save()

    def save(self) -> None:
        """Write out the project lockfile."""
        with self.path.open(mode="w") as lockfile:
            json.dump(self._checksums, lockfile)


class Project:
    """Represents a single Artix project configuration."""

    artifacts: dict[str, Artifact]
    lockfile: Lockfile
    repositories: dict[str, Repository]
    _root: Path

    def __init__(self, configuration: str, root: Path) -> None:
        """Initialize a project configuration from the given configuration."""
        self.artifacts = {}
        self.repositories = {}
        self._root = root
        self.lockfile = Lockfile(root=self.root)

        config_obj = tomli.loads(configuration)
        for name, definition in config_obj.get("repository", {}).items():
            self.repositories[name] = Repository(
                name=name,
                source=definition["source"],
            )

        for name, definition in config_obj.get("artifact", {}).items():
            self.artifacts[name] = Artifact(
                destination=self.root / definition.get("destination"),
                locked=definition.get("locked", True),
                name=name,
                repository=self.repositories.get(definition.get("repository")),
                version=definition.get("version", {}),
            )

    def __repr__(self) -> str:  # pragma: no cover
        """Return a string representation of the configuration."""
        return str(self.root)

    @staticmethod
    def from_path(path: Path) -> Project:
        """Return a project configuration instance from the given path."""
        # If the given path is a directory, assume we're going to read from the
        # artix.toml file in the directory.
        if path.is_dir():
            path /= "artix.toml"

        # Create our project configuration.
        with path.open(mode="rb") as configuration_file:
            return Project(
                configuration=configuration_file.read().decode(encoding="utf-8"),
                root=path.parent,
            )

    @property
    def root(self) -> Path:
        """Return the path to the root directory of the configuration."""
        return self._root

    def sync(self) -> bool:
        """Pull down the artifacts of the project."""
        # Iterate through each artifact and download them one by one.
        # NOTE: In the future we should look into pulling in parallel.
        overall_success = True
        for name, artifact in self.artifacts.items():
            loguru.logger.info(
                "syncing '{}' to {}",
                name,
                artifact.destination,
            )
            success = artifact.sync(expected=self.lockfile.checksum(artifact=artifact))
            overall_success = overall_success and success
            if not success:  # pragma: no cover
                loguru.logger.error("failed to sync artifact '{}'", artifact.name)
                continue

            # If the artifact is to be locked to the expected hash, save it to the
            # lockfile.
            if artifact.locked:
                self.lockfile.add(artifact=artifact)
        return overall_success
