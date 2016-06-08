Connecting
**********

The board you got should already have Micropython with all the needed libraries
flashed on it. In order to access its console, you will need to connect it to
your computer with the micro-USB cable, and access the serial interface that
appears with a terminal program.

Linux and MacOS
===============

Simply open a terminal and run the following command::

    screen /dev/ttyUSB0 115200

Windows
=======

For the serial interface to appear in your system, you will need to install the drivers_ for CP2102. Once you have that, you can use either Hyper Terminal or PuTTy to connect to it, following this guide_.

The parameters for the connection are: 115200 baud rate, 8 data bits, no parity, 1 stop bit, no flow control.

Hello world!
============

Once you are connected, press "enter" and you should see the Micropython prompt, that looks like this::

    >>>

It's traditional to start with a "Hello world!" program, so type this and press "enter"::

    print("Hello world!")

If you see "Hello world!" displayed in the next line, then congratulations, you got it working.

.. _drivers: http://www.silabs.com/products/mcu/Pages/USBtoUARTBridgeVCPDrivers.aspx
.. _guide: https://techawarey.wordpress.com/tag/serial-port-communication-in-windows-7-using-hyper-terminal-and-putty/
