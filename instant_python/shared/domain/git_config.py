from dataclasses import asdict, dataclass, field

from instant_python.shared.application_error import ApplicationError


@dataclass
class GitConfig:
    initialize: bool
    username: str | None = field(default=None)
    email: str | None = field(default=None)

    def __post_init__(self) -> None:
        self._ensure_username_and_email_are_set_if_initializing()

    def _ensure_username_and_email_are_set_if_initializing(self) -> None:
        if self.initialize and (self._username_is_not_specified() or self._email_is_not_specified()):
            raise GitUserOrEmailNotPresent()

    def _email_is_not_specified(self) -> bool:
        return self.email is None or self.email == ""

    def _username_is_not_specified(self) -> bool:
        return self.username is None or self.username == ""

    def to_primitives(self) -> dict[str, str | bool]:
        return asdict(self)


class GitUserOrEmailNotPresent(ApplicationError):
    def __init__(self) -> None:
        super().__init__(message="When initializing a git repository, both username and email must be provided.")
