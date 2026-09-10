from abc import ABC, abstractmethod

from instant_python.version.domain.latest_version import LatestVersion


class VersionRepository(ABC):
    @abstractmethod
    def get_latest_version(self) -> LatestVersion:
        raise NotImplementedError
