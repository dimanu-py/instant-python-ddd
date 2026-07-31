from instant_python.initialize.domain.version_control_configurer import VersionControlConfigurer
from instant_python.initialize.infra.env_manager.system_console import SystemConsole
from instant_python.shared.domain.git_config import GitConfig


class GitConfigurer(VersionControlConfigurer):
    def __init__(self, console: SystemConsole) -> None:
        self._console = console

    def setup(self, config: GitConfig) -> None:
        print(">>> Setting up git repository...")
        self._initialize_repository()
        self._set_user_information(
            username=config.username,
            email=config.email,
        )
        self._make_initial_commit()
        print(">>> Git repository created successfully")

    def _initialize_repository(self) -> None:
        self._console.execute_or_raise(command="git init")

    def _set_user_information(self, username: str, email: str) -> None:
        self._console.execute(command=f"git config user.name {username}")
        self._console.execute(command=f"git config user.email {email}")

    def _make_initial_commit(self) -> None:
        self._console.execute(command="git add .")
        self._console.execute(command='git commit -m "🎉 chore: initial commit"')
