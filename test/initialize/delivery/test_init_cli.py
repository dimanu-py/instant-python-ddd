import json
import os
import shutil
import tempfile
from collections.abc import Generator
from contextlib import contextmanager

import pytest
import yaml
from approvaltests import verify, verify_all_combinations
from typer.testing import CliRunner

from instant_python.initialize.delivery.cli import app
from instant_python.shared.supported_built_in_features import SupportedBuiltInFeatures
from instant_python.shared.supported_licenses import SupportedLicenses
from instant_python.shared.supported_managers import SupportedManagers
from instant_python.shared.supported_python_versions import SupportedPythonVersions
from instant_python.shared.supported_templates import SupportedTemplates
from test.utils import resources_path


@contextmanager
def _isolated_filesystem() -> Generator[None, None, None]:
    cwd = os.getcwd()
    tmp_dir = tempfile.mkdtemp()
    os.chdir(tmp_dir)
    try:
        yield
    finally:
        os.chdir(cwd)
        shutil.rmtree(tmp_dir)


@pytest.mark.acceptance
class TestInitCli:
    def setup_method(self) -> None:
        self._runner = CliRunner()

    def test_should_initialize_project_with_general_section_combinations(self) -> None:
        dependency_managers = SupportedManagers.get_supported_managers()
        licenses = SupportedLicenses.get_supported_licenses()
        python_versions = SupportedPythonVersions.get_supported_versions()

        verify_all_combinations(
            self._run_cli_with_general_config,
            [
                dependency_managers,
                licenses,
                python_versions,
            ],
        )

    def test_should_initialize_project_with_git_section_combinations(self) -> None:
        create_git_repository = [True, False]

        verify_all_combinations(
            self._run_cli_with_git_config,
            [
                create_git_repository,
            ],
        )

    def test_should_initialize_project_with_template_section_combinations(self) -> None:
        templates = SupportedTemplates.get_supported_templates()
        built_in_features = SupportedBuiltInFeatures.get_supported_built_in_features()

        verify_all_combinations(
            self._run_cli_with_template_config,
            [
                templates,
                built_in_features,
            ],
        )

    def test_should_initialize_project_with_predefined_dependencies_and_different_managers(self) -> None:
        dependency_managers = SupportedManagers.get_supported_managers()
        predefined_dependencies = [
            {"name": "requests", "version": "latest", "is_dev": False, "group": ""},
            {"name": "pytest", "version": "6.2.5", "is_dev": True, "group": "testing"},
        ]

        verify_all_combinations(
            self._run_cli_with_predefined_dependencies,
            [
                dependency_managers,
                predefined_dependencies,
            ],
        )

    def test_should_initialize_project_with_custom_project_structure(self) -> None:
        verify(
            self._run_cli_with_custom_template_config(
                template=SupportedTemplates.CUSTOM.value,
                custom_template_path=str(resources_path()),
            )
        )

    def _run_cli_with_general_config(
        self,
        dependency_manager: str,
        license_type: str,
        python_version: str,
    ) -> dict:
        config = self._create_general_config(
            dependency_manager=dependency_manager,
            license_type=license_type,
            python_version=python_version,
        )

        return self._run_cli_with_config(config)

    def _run_cli_with_git_config(
        self,
        initialize_git: bool,
    ) -> dict:
        config = self._create_git_config(
            initialize_git=initialize_git,
        )

        return self._run_cli_with_config(config)

    def _run_cli_with_template_config(
        self,
        template: str,
        built_in_feature: str,
    ) -> dict:
        config = self._create_template_config(
            template=template,
            built_in_feature=built_in_feature,
        )

        return self._run_cli_with_config(config)

    def _run_cli_with_predefined_dependencies(
        self,
        dependency_manager: str,
        predefined_dependency: dict,
    ) -> dict:
        config = self._create_general_config(
            dependency_manager=dependency_manager,
            license_type="MIT",
            python_version="3.10",
        )

        config["dependencies"] = [predefined_dependency]

        return self._run_cli_with_config(config)

    def _run_cli_with_custom_template_config(
        self,
        template: str,
        custom_template_path: str,
    ) -> dict:
        config = json.loads(json.dumps(self._read_base_config()))

        config["template"]["name"] = template

        return self._run_cli_with_custom_config(config, custom_template_path)

    def _run_cli_with_config(self, config: dict) -> dict:
        with tempfile.NamedTemporaryFile(mode="w", suffix=".yml", delete=False) as config_file:
            yaml.dump(config, config_file)
            config_file_path = config_file.name

        with _isolated_filesystem():
            result = self._runner.invoke(app, ["--config", str(config_file_path)])

        return {
            "exit_code": result.exit_code,
            "errors": result.exception,
        }

    def _run_cli_with_custom_config(self, config: dict, custom_template_folder: str) -> dict:
        with tempfile.NamedTemporaryFile(mode="w", suffix=".yml", delete=False) as config_file:
            yaml.dump(config, config_file)
            config_file_path = config_file.name

        with _isolated_filesystem():
            result = self._runner.invoke(
                app, ["--config", str(config_file_path), "--templates", str(custom_template_folder)]
            )

        return {
            "exit_code": result.exit_code,
            "errors": result.exception,
        }

    def _create_general_config(
        self,
        dependency_manager: str,
        license_type: str,
        python_version: str,
    ) -> dict:
        config = json.loads(json.dumps(self._read_base_config()))

        config["general"]["dependency_manager"] = dependency_manager
        config["general"]["license"] = license_type
        config["general"]["python_version"] = python_version

        return config

    def _create_git_config(
        self,
        initialize_git: bool,
    ) -> dict:
        config = json.loads(json.dumps(self._read_base_config()))

        config["git"]["initialize"] = initialize_git

        return config

    def _create_template_config(
        self,
        template: str,
        built_in_feature: str,
    ) -> dict:
        config = json.loads(json.dumps(self._read_base_config()))

        config["template"]["name"] = template
        config["template"]["built_in_features"] = [built_in_feature]

        return config

    @staticmethod
    def _read_base_config() -> dict:
        base_config_path = resources_path() / "base_ipy_config.yml"
        with base_config_path.open("r") as file:
            return yaml.safe_load(file)
