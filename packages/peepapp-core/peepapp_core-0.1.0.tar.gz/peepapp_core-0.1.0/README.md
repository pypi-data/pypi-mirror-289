# PeepApp core

[![Build Status](https://github.com/Exodus-Privacy/peepapp-core/actions/workflows/main.yml/badge.svg?branch=v1)](https://github.com/Exodus-Privacy/peepapp-core/actions/workflows/main.yml) [![CodeQL](https://github.com/Exodus-Privacy/peepapp-core/actions/workflows/codeql.yml/badge.svg)](https://github.com/Exodus-Privacy/peepapp-core/actions/workflows/codeql.yml)

Contains:

* Static analysis
* Network analysis
* Connection helper

## Installation

peepapp-core is available from [PyPI](https://pypi.org/project/peepapp-core):

```shell
pip install peepapp-core
```

## Include it to your project

Add the following line in your `requirements.txt` (replace 'XX' by the desired subversion):

```text
peepapp-core==XX
```

## Local usage

Clone this repository:

```shell
git clone https://github.com/Exodus-Privacy/peepapp-core.git
cd peepapp-core
```

### Using Docker

Build the Docker image:

```shell
docker build -t peepapp-core .
```

Run tests:

```shell
docker run -it --rm peepapp-core /bin/bash
python -m unittest discover -s peepapp_core -p "test_*.py"
```

### Manual installation

Install `dexdump`:

```shell
sudo apt-get install dexdump
```

Create Python `virtualenv`:

```shell
virtualenv venv -p python3
source venv/bin/activate
```

Install dependencies:

```shell
pip install -r requirements.txt
```

Run tests:

```shell
python -m unittest discover -s peepapp_core -p "test_*.py"
```
