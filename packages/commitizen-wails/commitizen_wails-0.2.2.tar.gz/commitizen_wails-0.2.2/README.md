# commitizen Wails Version Provider

A commitizen version provider for [Wails](https://wails.io).

![PyPI - Version](https://img.shields.io/pypi/v/commitizen-wails)
![PyPI - Status](https://img.shields.io/pypi/status/commitizen-wails)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/commitizen-wails)
![PyPI - Implementation](https://img.shields.io/pypi/implementation/commitizen-wails)
![PyPI - License](https://img.shields.io/pypi/l/commitizen-wails)

## Installation

```shell
pip install commitizen commitizen-wails
```

Via rye tools:

```shell
rye install commitizen --extra-requirement commitizen-wails
```

## Configuration

Example for `.cz.toml`

```toml
[tool.commitizen]
name = "cz_conventional_commits"
tag_format = "$version"
version_scheme = "semver"
version_provider = "wails-provider"
update_changelog_on_bump = true
major_version_zero = true
```

## License

This project is [MIT](./LICENSE) licensed.
