from instant_python.version.domain.latest_version import LatestVersion
from instant_python.version.domain.version_repository import VersionRepository


class LatestVersionPrinter:
    def __init__(self, version_repository: VersionRepository) -> None:
        self._version_repository = version_repository

    def execute(self) -> LatestVersion:
        return self._version_repository.get_latest_version()
