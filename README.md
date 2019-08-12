# MicroPython Workshop

The purpose of this repository is to make a Sphinx-based web guide for running a MicroPython workshop (which can then be hosted on [Read the Docs](https://readthedocs.org/)).

The purpose of the workshop will be to take someone that may be familiar with Python but has never used it on a microcontroller, and allow them to smoothly sail through the treacherous seas towards getting that first piece of code running that makes the hardware do something fun. From there it aims to provide the resources and guidance necessary to develop skills further and progress towards project-based learning.

## Installation

To build the documentation locally, you will need [Sphinx](https://www.sphinx-doc.org). This is most easily retrieved via `pip install -r requirements.txt`. This should ideally be done in the virtual environment of your choice - although note that you may need to add generated folders to the `exclude_patterns` list in `conf.py` to avoid them being included and then complained about by Sphinx during build.

## Building

Building should be as simple as `make html` once you've got access to Sphinx - both `Makefile` and `make.bat` are provided so all platforms should be covered.
