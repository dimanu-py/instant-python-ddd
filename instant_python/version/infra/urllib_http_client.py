import json
import urllib
from urllib.error import URLError


class UrllibHttpClient:
    _TIMEOUT_SECONDS = 3

    def request(self, url: str) -> str | None:
        try:
            with urllib.request.urlopen(url, timeout=self._TIMEOUT_SECONDS) as response:
                data = json.loads(response.read())
            return data["info"]["version"]
        except (URLError, TimeoutError, json.JSONDecodeError, KeyError):
            return None
