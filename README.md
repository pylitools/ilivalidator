# ilivalidator
Python package for [ilivalidator](https://github.com/claeis/ilivalidator).

Ilivalidator is compiled to a [native shared library](https://www.graalvm.org/latest/reference-manual/native-image/guides/build-native-shared-library/) with [GraalVM](https://graalvm.org). This Python package calls the native shared library.

The native shared libs are built with Github Actions and thus are available for macOS, Ubuntu and Windows (all OS are x86_64).

## Installation

```
pip install ilivalidator
```

## Run

```
from ilivalidator import Ilivalidator

valid = Ilivalidator.validate('tests/data/254900.itf')
print("The file is valid: {}".format(valid))
```

## Develop

### Requirements
On Ubuntu 22.04:

```
sudo apt update
sudo apt install python3-pip
sudo apt install python3.10-venv
sudo apt-get install unzip zip
sudo apt-get install build-essential libz-dev zlib1g-dev
```

The latter two are needed for SDKMan and GraalVM Native Image.

### Python setup

```
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade setuptools wheel
```

### Building

```
python3 setup.py sdist bdist_wheel
python3 setup.py sdist bdist_wheel --plat-name=manylinux2014_aarch64 
```

### Install locally

```
pip install -e .
pip install -e .[test]
```

### Running tests

```
pytest ilivalidator
```

### Dev environment

You can use Multipass for using Ubuntu as Development environment:

```
multipass launch jammy --cpus 4 --disk 20G --mem 8G --name python-ili-build
multipass mount $HOME/sources python-ili-build:/home/ubuntu/sources
multipass shell python-ili-build
multipass stop python-ili-build
```

Install Java:

```
curl -s "https://get.sdkman.io" | bash
source ...
sdk i java 22.3.r17-grl
```

## Todo
- Tests: Wie kann die shared lib getestet werden? 