Introduction
************

MicroPython
===========
MicroPython is a lean and efficient implementation of the Python 3 programming
language that includes a small subset of the Python standard library and is
optimised to run on microcontrollers and in constrained environments.

MicroPython is packed full of advanced features such as an interactive prompt,
arbitrary precision integers, closures, list comprehension, generators,
exception handling and more. Yet it is compact enough to fit and run within
just 256k of code space and 16k of RAM.

MicroPython aims to be as compatible with normal Python as possible to allow
you to transfer code with ease from the desktop to a microcontroller or
embedded system.

Workshop
========

This workshop is intended to get you started experimenting with hardware *as
quickly as possible*! It's our experience that one of the best ways to get
started with MicroPython is to simply *use it on a device*.

It's based around using *Shields*. Shields allow peripherals to be easily
connected to the microcontroller to extend functionality in interesting ways
such as by illuminating LEDs, connecting sensors and buttons for input, or
outputting to displays.

The shields are built for a developer board called the *Wemos D1 Mini*,
originally built around an ESP8266 microcontroller. These boards became
very popular and so shields for them are readily available and inexpensive.
Instead of the original ESP8266 board, a much more powerful microcontroller -
an ESP32 - was chosen for this workshop. The development board is known as
the *TTGO Mini 32* board and it matches the pin layout of the Wemos D1 Mini
so all the existing shields can be used.

Shields are *perfect* for a starter workshop since there's no need
to solder components together or even use a breadboard. Just plug the shield
in to the microcontroller board and get going! Many shields are available
inexpensively online.

In general, each page that describes a shield will walk through the basics
of how to interact with it and then propose exercises to work
through. Generally the exercises increase in difficulty.

Let's get to it!
