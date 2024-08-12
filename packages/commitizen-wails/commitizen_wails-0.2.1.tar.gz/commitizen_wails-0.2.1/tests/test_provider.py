import json
from pathlib import Path

from commitizen.config import BaseConfig
from pytest_mock import MockerFixture

from commitizen_wails.provider import WailsVersionProvider

wails_json = """
{
  "$schema": "https://wails.io/schemas/config.v2.json",
  "name": "commitizen-wails",
  "outputfilename": "commitizen-wails",
  "frontend:install": "pnpm install",
  "frontend:build": "pnpm run build",
  "frontend:dev:watcher": "pnpm run dev",
  "frontend:dev:serverUrl": "auto",
  "author": {
    "name": "YogiLiu",
    "email": "YogiLiu@outlook.com"
  }
}
"""

wails_json_with_version = """
{
  "$schema": "https://wails.io/schemas/config.v2.json",
  "name": "commitizen-wails",
  "outputfilename": "commitizen-wails",
  "frontend:install": "pnpm install",
  "frontend:build": "pnpm run build",
  "frontend:dev:watcher": "pnpm run dev",
  "frontend:dev:serverUrl": "auto",
  "author": {
    "name": "YogiLiu",
    "email": "YogiLiu@outlook.com"
  },
  "info": {
    "productVersion": "0.0.1"
  }
}
"""


def read_text(
    self: Path, encoding: str | None = None, errors: str | None = None
) -> str:
    return wails_json


def read_version_text(
    self: Path, encoding: str | None = None, errors: str | None = None
) -> str:
    return wails_json_with_version


class MockedWriter:
    def __init__(self):
        self.config = None

    def __call__(self, config: str):
        self.config = config


def test_get_version_empty(mocker: MockerFixture):
    mocker.patch("pathlib.Path.read_text", read_text)
    vp = WailsVersionProvider(BaseConfig())
    assert vp.get_version() == "0.0.1"


def test_get_version(mocker: MockerFixture):
    mocker.patch("pathlib.Path.read_text", read_version_text)
    vp = WailsVersionProvider(BaseConfig())
    assert vp.get_version() == "0.0.1"


def test_set_version_empty(mocker: MockerFixture):
    mocker.patch("pathlib.Path.read_text", read_text)
    w = MockedWriter()
    mocker.patch("pathlib.Path.write_text", w)
    vp = WailsVersionProvider(BaseConfig())
    vp.set_version("0.100.0")
    assert w.config is not None
    assert json.loads(w.config)["info"]["productVersion"] == "0.100.0"


def test_set_version(mocker: MockerFixture):
    mocker.patch("pathlib.Path.read_text", read_version_text)
    w = MockedWriter()
    mocker.patch("pathlib.Path.write_text", w)
    vp = WailsVersionProvider(BaseConfig())
    vp.set_version("0.1.0")
    assert w.config is not None
    assert json.loads(w.config)["info"]["productVersion"] == "0.1.0"
