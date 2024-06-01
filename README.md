# Selenium + python

## Prepare

- install [python](https://www.python.org/)
- install [poetry](https://python-poetry.org/)
- be certain has one of installed browser Chrome or Firefox

## Usage

You can change value in config file (conftest.py), or provide env
variables

### Linux or MacOS

```bash
export BASE_URL="www.your.url"
```

### Windows powershell

```bash
$env:BASE_URL="www.your.url"
```

### Windows cmd

```bash
set BASE_URL = "www.your.url"
```

## Start

```shell
poetry shell
poetry install
pytest --browser_name chrome
```
