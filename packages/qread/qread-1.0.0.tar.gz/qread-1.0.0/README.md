# qread
[![PyPi Version](https://img.shields.io/pypi/v/qread.svg)](https://pypi.python.org/pypi/qread)
[![PyPI Status](https://img.shields.io/pypi/status/qread.svg)](https://pypi.python.org/pypi/qread)
[![Python Versions](https://img.shields.io/pypi/pyversions/qread.svg)](https://pypi.python.org/pypi/qread)
[![License](https://img.shields.io/github/license/ReK42/qread)](https://github.com/ReK42/qread/blob/main/LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/ReK42/qread/main?logo=github)](https://github.com/ReK42/qread/commits/main)
[![Build Status](https://img.shields.io/github/actions/workflow/status/ReK42/qread/build.yml?logo=github)](https://github.com/ReK42/qread/actions)

Read a QR code from an image file.

## Installation
Install [Python](https://www.python.org/downloads/), then install [pipx](https://github.com/pypa/pipx) and use it to install `qread`:
```sh
pipx install qread
```

## Usage
```sh
qread <qr code image file>
```

For all options, run `qread --help`

## Development Environment
### Installation
```sh
git clone https://github.com/ReK42/qread.git
cd qread
python -m venv .env
source .env/bin/activate
python -m pip install --upgrade pip pre-commit
pre-commit install
pip install -e .[test]
```

### Manual Testing
To check:
```sh
mypy src
ruff check src
ruff format --diff src
```

To auto-fix/format:
```sh
ruff check --fix src
ruff format src
```

### Manual Building
```sh
pip install -e .[build]
python -m build
```
