# Citrand

PRNG manipulation aide for emulated Pokémon 3DS titles.

[![Codeberg](https://img.shields.io/badge/Repository-Codeberg-blue?logo=codeberg&labelColor=white&style=plastic)](https://codeberg.org/ViteByte/citrand/)
[![CPython 3.10+](https://img.shields.io/badge/CPython-3.10_|_3.11_|_3.12-blue?style=plastic)](https://www.python.org/downloads/)
[![PyPI Version](https://img.shields.io/pypi/v/citrand?label=PyPI&color=blue&style=plastic)](https://pypi.org/project/citrand)
[![GPLv3+ License](https://img.shields.io/pypi/l/citrand?label=License&color=blue&style=plastic)](https://codeberg.org/ViteByte/citrand/raw/branch/main/LICENSE)

## Installation

Requirements for running Citrand:
- [Python](https://www.python.org/downloads/) (version `3.10` or greater)
- [Pipx](https://pypi.org/project/pipx/) or [Pip](https://pypi.org/project/pip/)
- [Git](https://git-scm.com/) (optional)

### Codeberg (recommended)

The Codeberg repository contains the latest improvements for Citrand, but it
may include bugs or stability issues.

This method requires `git` in order to download the package files from the
repository.

```bash
# SSH
python3 -m pipx install git+ssh://git@codeberg.org/ViteByte/citrand.git
# HTTPS
python3 -m pipx install git+https://codeberg.org/ViteByte/citrand.git
```

### Python Package Index

PyPI provides the most stable release, but may lack newer features or
bug fixes.

```shell
python3 -m pipx install citrand
```
