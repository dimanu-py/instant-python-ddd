from dataclasses import dataclass


@dataclass
class LatestVersion:
    version: str

    @classmethod
    def unknown(cls) -> "LatestVersion":
        return cls("unknown")

    def __repr__(self) -> str:
        return self.version
