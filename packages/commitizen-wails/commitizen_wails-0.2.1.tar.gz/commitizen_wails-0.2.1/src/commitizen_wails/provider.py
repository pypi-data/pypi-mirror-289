import json
from pathlib import Path
from commitizen.providers import VersionProvider

from .types import Config, Info


class WailsVersionProvider(VersionProvider):
    _path = Path(".") / "wails.json"
    _default_version = "0.0.1"

    def _get_config(self) -> Config:
        return json.loads(self._path.read_text())

    def get_version(self) -> str:
        config = self._get_config()
        info = config.get("info", Info(productVersion=self._default_version))
        return info.get("productVersion", self._default_version)

    def set_version(self, version: str):
        config = self._get_config()
        info = config.setdefault("info", Info(productVersion=self._default_version))
        info["productVersion"] = version
        self._path.write_text(json.dumps(config, indent=2, ensure_ascii=False))
