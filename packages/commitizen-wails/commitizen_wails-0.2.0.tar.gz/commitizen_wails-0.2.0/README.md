# commitizen Wails Version Provider

A commitizen version provider for [Wails](https://wails.io).

## Installation

```shell
pip install commitizen commitizen-wails
```

Via rye tools:

```shell
rye install commitizen --extra-requirement commitizen-wails
```

## Configuration

Example for `.cz.yaml`

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
