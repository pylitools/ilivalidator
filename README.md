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

valid = Ilivalidator.validate(['path/to/foo.xtf'])
print("The file is valid: {}".format(valid))
```

Options are set with a dictionary:

```
from ilivalidator import Ilivalidator

settings = {Ilivalidator.SETTING_ALL_OBJECTS_ACCESSIBLE: True}
valid = Ilivalidator.validate(["file1.xtf","file2.xtf"], settings)
```

Supported options:

| Python package | Ilivalidator |
| --- | --- |
| `SETTING_ILIDIRS` | `--modeldir` |
| `SETTING_MODELNAMES` | `--models` |
| `SETTING_ALL_OBJECTS_ACCESSIBLE` | `--allObjectsAccessible` |
| `SETTING_LOGFILE` | `--log` |
| `SETTING_LOGFILE_TIMESTAMP` | `--logtime` |
| `SETTING_XTFLOG` | `--xtflog` |
| `trace` | `--trace` |

You have to use `True/False` for options without arguments, e.g. `SETTING_ALL_OBJECTS_ACCESSIBLE`.

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
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade setuptools wheel
```

### Building

```
python3 setup.py sdist bdist_wheel
python3 setup.py sdist bdist_wheel --plat-name=manylinux2014_aarch64 
python3 setup.py sdist bdist_wheel --plat-name=manylinux2014_x86_64 
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
multipass launch jammy --cpus 4 --disk 20G --memory 8G --name pylitools-dev
multipass mount $HOME/sources pylitools-dev:/home/ubuntu/sources
multipass shell pylitools-dev
multipass stop pylitools-dev
```

Install Java:

```
sudo apt-get update 
sudo apt-get install gcc zlib1g-dev build-essential zip unzip

curl -s "https://get.sdkman.io" | bash
source "/home/ubuntu/.sdkman/bin/sdkman-init.sh"
sdk i java 21-graalce
```

Compile shared lib:
```
./gradlew clean test nativeCompile
```
`JAVA_HOME` muss gesetzt sein. Notfalls einmal aus- und einloggen, wenn man in der gleichen Session Java installiert hat.


## Todo
- Tests: Wie kann die shared lib getestet werden? 