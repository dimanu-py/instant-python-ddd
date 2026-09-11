import pytest
from doublex import Mimic, Mock, expect_call
from doublex_expects import have_been_satisfied
from expects import equal, expect

from instant_python.version.domain.latest_version import LatestVersion
from instant_python.version.infra.py_pi_version_repository import PyPiVersionRepository
from instant_python.version.infra.urllib_http_client import UrllibHttpClient


@pytest.mark.integration
class TestPyPiVersionRepository:
    _PYPI_URL = "https://pypi.org/pypi/instant-python/json"
    _ANY_VERSION = "1.0.0"

    def setup_method(self) -> None:
        self._http_client = Mimic(Mock, UrllibHttpClient)
        self._pypi_version_repository = PyPiVersionRepository(self._http_client)

    def test_should_get_response_from_pypi(self) -> None:
        expect_call(self._http_client).request(self._PYPI_URL).returns(self._ANY_VERSION)

        self._pypi_version_repository.get_latest_version()

        expect(self._http_client).to(have_been_satisfied)

    def test_should_should_get_pypi_latest_version(self) -> None:
        expect_call(self._http_client).request(self._PYPI_URL).returns(self._ANY_VERSION)

        latest_version = self._pypi_version_repository.get_latest_version()

        expect(latest_version).to(equal(LatestVersion(self._ANY_VERSION)))

    def test_should_get_unknown_latest_version_when_pypi_fails(self) -> None:
        expect_call(self._http_client).request(self._PYPI_URL).returns(None)

        latest_version = self._pypi_version_repository.get_latest_version()

        expect(latest_version).to(equal(LatestVersion.unknown()))
