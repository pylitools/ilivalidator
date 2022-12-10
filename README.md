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
tbd

## Todo
- Tests: Wie kann die shared lib getestet werden? 