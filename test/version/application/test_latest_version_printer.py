from doublex import Mock, expect_call
from expects import equal, expect

from instant_python.version.application.latest_version_printer import LatestVersionPrinter
from instant_python.version.domain.latest_version import LatestVersion
from instant_python.version.domain.version_repository import VersionRepository


class TestLatestVersionPrinter:
    def test_should_return_latest_version(self) -> None:
        version_repository = Mock(VersionRepository)
        version_printer = LatestVersionPrinter(version_repository=version_repository)
        expected_version = LatestVersion("1.1.1")
        expect_call(version_repository).get_latest_version().returns(expected_version)

        latest_version = version_printer.execute()

        expect(latest_version).to(equal(expected_version))

    def test_should_return_unknown_when_latest_version_is_not_reachable(self) -> None:
        version_repository = Mock(VersionRepository)
        version_printer = LatestVersionPrinter(version_repository=version_repository)
        expected_version = LatestVersion("unknown")
        expect_call(version_repository).get_latest_version().returns(expected_version)

        latest_version = version_printer.execute()

        expect(latest_version).to(equal(expected_version))
