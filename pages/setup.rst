Setup
*****

Prerequisites
=============

To participate in the workshop, you will need the following:

  * A laptop with Linux, Mac OS or Windows and at least one free USB port.
  * If it's Windows or Mac OS, make sure to install `drivers`_ for the CH340
    USB to Serial chip. MacOS El Capitan may require `disabling kext signing`_
    to install it.
  * A micro-USB cable (with data lines) that fits your USB port.
  * You will need a terminal application installed. For Linux and Mac you can
    use ``screen``, which is installed by default. For Windows we recommend
    `PuTTy`_ or `TeraTerm`_.
  * Please note that the workshop will be in English.

.. _drivers: https://wiki.wemos.cc/downloads
.. _disabling kext signing: http://farazmemon.com/2016/02/07/flashing-latest-firmware-on-nodemcu-devkit-v0-9-osx-el-capitan/
.. _PuTTy: http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html
.. _TeraTerm: https://ttssh2.osdn.jp/index.html.en

In addition, at the workshop, you will receive:
  * "WEMOS D1 Mini" development board (with an ESP8266 at the heart of it)
  * RGB LED Shield
  * LED Matrix Shield

Other Shields will be available for use during the workshop (but at lower
numbers, sharing is caring!).

The firmware that is flashed on the boards is also available at https://micropython.org/download#esp8266


Development Board
=================

The board we are using is called a "WEMOS D1 Mini" which has an ESP8266 module
on it, which we will be programming. It comes with the latest version of
MicroPython already setup on it, together with all the drivers we are going
to use.

.. note::
    The D0, D1, D2, ... numbers printed on the board are different from what
    MicroPython uses -- because originally those boards were made for a
    different software. Make sure to refer to the image below to determine
    which pins are which.

.. image:: /images/wemos_d1_mini_top.png


On top it has a micro-USB socket, for connecting to the computer. Next to it
is a reset button. Then on both sides of the
board are two rows of pins, to which we will be connecting the shields.

The symbols meaning is as follows:

  * ``3v3`` - this is a fancy way to write 3.3V, which is the voltage that the
    board runs on internally. You can think about this pin like the plus side
    of a battery. There are several pins like this, they are all connected
    inside.
  * ``gnd`` - this is the ground. Think about it like the minus side of the
    battery. They are also all connected.
  * ``Dx`` - These are "Digital" pins, or "GPIO"s (which stands for "General
    Purpose Input Output"). Those are the pins we will be using for sending and
    receiving signals to and from various devices that we will connect to them.
    They can act as output -- pretty much like a switch that you can connect to
    plus or to minus with your program.  Or they can act as input, telling your
    program whether they are connected to plus or minus.
  * ``A0`` - this is the analog pin. It can measure the voltage that is applied
    to it, but it can only handle up to 1V.
  * ``5v0`` - this pin is connected with the 5V from your computer. You can
    also use it to power your board with a battery when it's not connected to
    the computer. The voltage applied here will be internally converted to the
    3.3V that the board needs.
  * ``RX`` / ``TX`` - these are connected to the UART port used for device
    communications. This UART port is the one also used by the USB to
    ommunicate with the device from your PC, so don't connect anything to these
    pins or your USB communications might have problems!
  * ``RST`` - this is a reset pin (connected to the corresponding RESET
    button).


Connecting
==========

The board you got should already have MicroPython with all the needed libraries
flashed on it. In order to access its console, you will need to connect it to
your computer with the micro-USB cable, and access the serial interface that
appears with a terminal program.


Linux and MacOS
---------------

Simply open a terminal and run the following commands. On Linux::

    screen /dev/ttyUSB0 115200

On MacOS::

    screen /dev/tty.SLAB_USBtoUART 115200

To exit screen, press ctrl+A and then capital K.


Windows
-------

For the serial interface to appear in your system, you will need to install the
drivers_ for CP2102. Once you have that, you can use either Hyper Terminal,
PuTTy or CoolTerm to connect to it, following this guide_.

The parameters for the connection are: 115200 baud rate, 8 data bits, no
parity, 1 stop bit, no flow control.


Hello world!
------------

Once you are connected, press "enter" and you should see the MicroPython
prompt, that looks like this::

    >>>

It's traditional to start with a "Hello world!" program, so type this and
press "enter"::

    print("Hello world!")

If you see "Hello world!" displayed in the next line, then congratulations,
you got it working.

.. _guide: https://techawarey.wordpress.com/tag/serial-port-communication-in-windows-7-using-hyper-terminal-and-putty/


Official Documentation and Support
==================================

The official documentation for this port of MicroPython is available at
http://micropython.org/resources/docs/en/latest/esp8266/.

There is a also a forum on which you can ask questions and get help, located at
http://forum.micropython.org/.

Finally, there is a MicroPython Slack channel that you can join at
https://slack-micropython.herokuapp.com/, where people chat in real time.
