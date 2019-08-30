Setup
*****

Prerequisites
=============

To participate in the workshop, you will need the following:

  * A laptop with Linux, Mac OS or Windows and at least one free USB port.
  * If it's Windows or Mac OS, make sure to install `drivers`_ for the CH340
    USB to Serial chip. MacOS El Capitan may require `disabling kext signing`_
    to install it.
  * A terminal application installed. For Linux and Mac you can
    use ``screen``, which is installed by default. For Windows we recommend
    `TeraTerm`_ or `PuTTy`_.
  * Python, with a module for allowing file transfer to MicroPython devices.
    `rshell`_ is the recommended tool for Linux / Mac (doesn't play nice with
    Windows), and `mpfshell`_ is the recommended tool for Windows.
  * A micro-USB cable (with data lines) that fits your USB port.

.. _drivers: https://wiki.wemos.cc/downloads
.. _disabling kext signing: http://farazmemon.com/2016/02/07/flashing-latest-firmware-on-nodemcu-devkit-v0-9-osx-el-capitan/
.. _TeraTerm: https://ttssh2.osdn.jp/index.html.en
.. _PuTTy: http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html
.. _rshell: https://github.com/dhylands/rshell
.. _mpfshell: https://github.com/wendlers/mpfshell
.. _ampy: https://github.com/pycampers/ampy

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

.. image:: /images/wemos_d1_mini_top.PNG


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

The parameters for the connection are: 115200 baud rate, 8 data bits, no
parity, 1 stop bit, no flow control.


Linux and MacOS
---------------

Simply open a terminal and run the following commands. On Linux::

    screen /dev/ttyUSB0 115200

On MacOS::

    screen /dev/tty.SLAB_USBtoUART 115200

To exit screen, press ctrl+A and then capital K.


Windows
-------

To connect to the device, we'll need to know the serial port identifier, or
COM port, of the device. First of all, ensure your Wemos D1 Mini is connected
to your computer or else the port will not appear. The initial connection
may take several minutes for the device driver to properly work it's magic
and make the port appear, so monitor the device installation icon in the
taskbar to see when it's ready to go!

The port can be then found by looking in the Device Manager - the easiest way
to get there is to search ``dev man`` in the Start menu search.
If this does not work, there is a `Lifewire article`_ that details how to find
the Device Manager in various versions of Windows.

.. _Lifewire article: https://www.lifewire.com/how-to-open-device-manager-2626075#mntl-sc-block_1-0-9

Once in the Device Manager, the active serial ports for your computer can be
found under the "Ports" category, with the name of the port (which we will use
for connecting to the device) in brackets after the name of the device
(of the form COMx on Windows). If more than one device is in the Port list,
the easiest way to determine the right one may simply to be to unplug and
re-plug the device.

For Tera Term, this connection can be made going to File -> New Connection
(if the New Connection window doesn't open by default), select Serial, and then
select the COM port previously found. The baud rate is set incorrectly by
default, and so you may need to go to Setup -> Serial Port and set the
Baud rate to 115200.


Hello world!
------------

Once you are connected, press "enter" and you should see the MicroPython
interactive terminal (or `REPL`_)  prompt, that looks like this::

    >>>

.. _REPL: https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop

It's traditional to start with a "Hello world!" program, so type this and
press "enter"::

    print("Hello world!")

If you see "Hello world!" displayed in the next line, then congratulations!
You got it working.

Note that your computer sleeping / closing your laptop lid may cause the
connection to the Wemos D1 Mini to terminate - if your terminal appears to be
unresponsive, ensure that the communication port is still open, and reopen it
if not!


Running Scripts
===============

The MicroPython REPL is very powerful for running specific commands, but for
repeatedly running commands it can get pretty messy. If you have a script
that you just want to run once, it might be easiest just to copy the code
into the REPL. Pressing Ctrl+E will put the device into "Paste Mode" which will
neatly retain the formatting and only run once Paste Mode is exited by 
pressing Ctrl+D.

If a script is to be run repeatedly however, it likely makes more sense to
put the script into a file on the MicroPython internal file system. On startup,
A MicroPython device will search for a file named ``boot.py`` and run it if it is
found. Following this, the same will be done for ``main.py``. Upon completion of
both of these files (successfully or otherwise), the REPL will begin.


File Transfer
-------------

In order for the device to run your script on startup, or to enable importing
of modules into the MicroPython workspace, you will need to put the appropriate
files on the device.

First, we'll make a file that will be run on device startup. Make a file
named ``main.py`` in your current directory, and put the "hello world" text
from above into the file. This will make the device print "Hello World!" before
entering the REPL.

Then we need to put this file onto the device. The easiest way to do this, via
`mpfshell``` or ``rshell``, will be to connect to your board (make sure any other
terminals to your board are closed, such as the one used for your "Hello
world" test earlier!), and then copy the files across, such as below for
``rshell``::

    rshell -p PORT
    cp main.py /flash

or as follows for ``mpfshell``::

    python -m mp.mpfshell
    open PORT
    put main.py

Where ``PORT`` will be the device connection to your computer (something like
``COM1`` on windows, or ``/dev/ttyACM0`` on MAC / Linux).



Official Documentation and Support
==================================

The official documentation for this port of MicroPython is available at
http://docs.micropython.org/en/latest/esp8266/quickref.html.

There is a also a forum on which you can ask questions and get help, located at
http://forum.micropython.org/.

Finally, there is a MicroPython Slack channel that you can join at
https://slack-micropython.herokuapp.com/, where people chat in real time.
