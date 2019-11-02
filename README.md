# MicroPython Workshop

The purpose of this repository is to make a Sphinx-based web guide for running a
MicroPython workshop. This is hosted on [Read the
Docs](https://micropython-workshop.readthedocs.io/en/latest/).

The workshop targets someone that may be familiar with Python but is new to
MicroPython - or even embedded development entirely. The purpose is to gently
guide them towards getting that first piece of code running that makes the
hardware do something fun. From there it aims to provide the resources and
guidance necessary to develop skills further and progress towards project-based
learning.

## Installation

[Sphinx](https://www.sphinx-doc.org) is used to build the documentation. To
install using `virtualenv`:

```bash
> python -m venv env
> source env/bin/activate
> pip install -r requirements.txt
```

## Building

Build HTML with `make html` - both `Makefile` and `make.bat` are provided so all
platforms should be covered. The output directory is `_build/html`, simply open
`index.html` with a browser to view the workshop docs.
