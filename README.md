# greps
[![Tests](https://github.com/royreznik/greps/actions/workflows/tests.yml/badge.svg)](https://github.com/royreznik/greps/actions/workflows/tests.yml)
![GitHub License](https://img.shields.io/github/license/royreznik/greps)
[![codecov](https://codecov.io/gh/royreznik/greps/graph/graph/badge.svg?token=60063VB6J2)](https://codecov.io/gh/royreznik/greps)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/greps)
![Code style](https://img.shields.io/badge/code%20style-black-black)

greps is a super simple ipython magic that allow you to use `grep` over IPython output.

## installation
```bash
pip install greps
```
manually loading:
```ipython
# Inside an IPython shell
%load_ext greps
```
Automatic loading:
```bash
echo "c.InteractiveShellApp.extensions = ['greps']" > ~/.ipython/profile_default/ipython_config.py
```


## Usage
On previous output:
```ipython
In [1]: {i:i for i in range(3)}
Out[1]: 
{0: 0,
 1: 1,
 2: 2,
}
 
In [2]: %greps 1
Out[2]: ' 1: 1,\n'
```

On specific output line:
```ipython
In [1]: 1
Out[1]: 1

In [2]: 2
Out[2]: 2

In [3]: 3
Out[3]: 3

In [4]: 4
Out[4]: 4

In [5]: %greps -l 2 2
Out[5]: '2\n'
```
