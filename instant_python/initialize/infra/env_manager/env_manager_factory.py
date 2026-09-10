from instant_python.initialize.domain.env_manager import EnvManager
from instant_python.initialize.infra.env_manager.system_console import SystemConsole
from instant_python.initialize.infra.env_manager.uv_env_manager import UvEnvManager
from instant_python.shared.application_error import ApplicationError
from instant_python.shared.supported_managers import SupportedManagers


class EnvManagerFactory:
    @staticmethod
    def create(dependency_manager: str, console: SystemConsole) -> EnvManager:
        managers = {
            SupportedManagers.UV: UvEnvManager,
        }
        try:
            return managers[SupportedManagers(dependency_manager)](console=console)
        except KeyError:
            raise UnknownDependencyManagerError(dependency_manager)


class UnknownDependencyManagerError(ApplicationError):
    def __init__(self, manager: str) -> None:
        supported_managers = ".".join(SupportedManagers.get_supported_managers())
        super().__init__(
            message=f"Unknown env manager: {manager}. Please use some of the supported managers: '{supported_managers}'."
        )
