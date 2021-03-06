Setup
*****

Prerequisites
=============

To participate in the workshop, you will need the following:

  * A laptop with Linux, Mac OS or Windows and at least one free USB port.

    * A USB Type A to Micro B cable is provided as part of the workshop kit,
      however if your laptop only has USB-C ports then bring along either a
      USB-C to Micro B cable or a USB-C to USB Type A socket dongle.

  * If it's Windows or Mac OS, make sure to install `drivers`_ for the CH340
    USB to Serial chip. MacOS El Capitan may require disabling "kext signing"
    to install it.

  * If your OS is Linux-based then, depending on the distribution, you may need
    to configure a *user* to have *permission* to access the serial port. This
    is usually performed by adding a user to a *group* that controls access to
    the serial ports; on many distributions this is the *dialout* group::

      sudo adduser [user] dialout

    Replace ``[user]`` with the name of the user that should have access to the
    serial port. It's typically necessary to log out and then back in again.

  * `Mu`_ installed on your laptop. This will be used for writing code,
    transferring code to the device, and even running an interactive terminal
    directly on the microcontroller.

    * You will need to install the alpha of the next version of Mu (found in
      the box at the top of the download page) in order to work with the
      microcontroller we're using in the workshop, so make sure you grab this
      one!
      Unfortunately they don't provide prebuilt binaries of this for Linux
      distros, so if that's your weapon of choice you will have to
      `build from source`_ - condensed set of instructions::

        git clone https://github.com/mu-editor/mu.git
        cd mu
        python -m venv env
        source env/bin/activate
        pip install -e ".[dev]"
        python run.py

.. _drivers: https://wiki.wemos.cc/downloads
.. _Mu: https://codewith.mu
.. _build from source: https://mu.readthedocs.io/en/latest/#quickstart

In addition, at the workshop, you will receive:
  * "TTGO MINI 32" development board (with an ESP32 at the heart of it)
  * RGB LED Shield

Other Shields will be available for use during the workshop (but at lower
numbers, sharing is caring!).

The firmware that is flashed on the boards is also available at
https://micropython.org/download#esp32


Development Board
=================

The board we are using is called a "TTGO MINI 32" which has an ESP32 module
on it, which we will be programming. It comes with the latest version of
MicroPython already setup on it, together with all the drivers we are going
to use.

.. note::
    The numbers printed next to the pins on the bottom of the board are
    different from what we're going to be using - this is because the shields
    we're using have a different pin numbering scheme (which can be seen
    printed on the shields next to the pins). We're going to use a module to
    map these, so we can just use the pin names the shields use.

On top it has a micro-USB socket, for connecting to the computer. On the side
is a reset button. Then on each side of the board are two rows of pins - the
inside row of which we will be connecting the shields to.

There are many symbols next to the pins on the underside of the board. The
numbers are pin numbers we can use to control those particular pins. Some of
the other important symbols are as follows:

  * ``3V3`` - this is a fancy way to write 3.3V, which is the voltage that the
    board runs on internally. You can think about this pin like the plus side
    of a battery. There are several pins like this, they are all connected
    inside.
  * ``GND`` - this is the ground. Think about it like the minus side of the
    battery. They are also all connected.
  * ``5V`` - this pin is connected with the 5V from your computer. You can
    also use it to power your board with a battery when it's not connected to
    the computer. The voltage applied here will be internally converted to the
    3.3V that the board needs.
  * ``RXD`` / ``TXD`` - these are connected to the UART port used for device
    communications. This UART port is the one also used by the USB to
    ommunicate with the device from your PC, so don't connect anything to these
    pins or your USB communications might have problems!
  * ``RST`` - this is a reset pin (connected to the corresponding RESET
    button).


Connecting
==========

The board you got should already have MicroPython with all the needed libraries
flashed on it - so let's get started, and open up Mu (which hopefully you
already have installed from the Prerequisites section, if not, get it now!).
The first thing that should appear is a window asking what type of code or
device we're using - select the ESP MicroPython option. If you can't find this
option, you may not have the alpha version necessary! Make sure the top bar of
the window shows the version as Mu 1.1.0.alpha (or later). If you've selected
another option (or used Mu for something else previously) then press the Mode
button to bring the selection menu up again.

Now plug your TTGO MINI 32 into your laptop via the Micro USB cable, and you
should see a "Detected new ESP MicroPython device" message in the bottom left
and corner of the Mu window (note: this could take a couple of minutes if it
is the first time you're plugging the device in, especially if you're on
Windows). Once you see the message, press the REPL button at the top of the
Mu window - a terminal should appear at the bottom of the Mu window with a
messsage about MicroPython.

If you instead get "Could not find an attached device." message box, review
your connections and make sure you've got the driver installed before finally
unplugging and replugging the device. Hopefully one of these things identify
the issue at hand!


Hello world!
------------

Once you have your terminal to your microcontroller, click in the terminal and
press "enter" and you should see the MicroPython interactive terminal
(or `REPL`_)  prompt, that looks like this::

    >>>

.. _REPL: https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop

It's traditional to start with a "Hello world!" program, so type this and
press "enter"::

    print("Hello world!")

If you see "Hello world!" displayed in the next line, then congratulations!
You got it working.


Running Scripts
===============

The MicroPython REPL is very powerful for running specific commands, but for
repeatedly running commands it can get pretty messy. Mu makes life easy in this
regard, by providing the ability to write scripts directly in the editor, and
then simply press a button to run the script on the device. If you instead
wrote ``print("Hello Mu!")`` under the ``# Write your code here :-)`` message
in the editor, then you can simply press the Run button to run the code on the
device - you should see `Hello Mu!` appear in the terminal from your script
running.

If a script is to be run whenever the device is powered however, it likely
makes more sense to put the script into a file on the MicroPython internal
file system. On startup, A MicroPython device will search for a file named
``boot.py`` and run it if it is found. Following this, the same will be done
for ``main.py``. Upon completion of both of these files (successfully or
otherwise), the REPL will begin.


File Transfer
-------------

In order for the device to run your script on startup, or to enable importing
of modules into the MicroPython workspace, you will need to put the appropriate
files on the device.

In order to access the file browser in Mu, click the REPL button to close it.
This enables the Files button - if you now press that you will see the files
on the device, and the files in the Mu folder on your computer (likely empty).
You can't edit files directly on the device, but if you drag a file from the
device box to your computer box it will copy if from the device to your
computer, and then you can right click on it and "Open in Mu" to edit it.

Note that you can either see the REPL *or* the File browser, not both at
the same time - if the button for what you want is disabled, something is
probably already open and taking up the real estate.

For an example of file browser utility, if you retrieve and open the
``d1_mini.py`` file that we're going to use during the workshop for shield
interaction, you will see that there is no magic there, just mapping numbers to
more human-comprehensible names.

We can use this process to go the other way - if you create a new file in
Mu, add the line ``print("MicroPython is pretty neat")`` to it, save it as
``main.py`` and then drag it from your computer onto your device, then
every time the device resets, it will now print your message on startup.



Official Documentation and Support
==================================

The official documentation for this port of MicroPython is available at
http://docs.micropython.org/en/latest/esp32/quickref.html.

There is a also a forum on which you can ask questions and get help, located at
http://forum.micropython.org/.

Finally, there is a MicroPython Slack channel that you can join at
https://slack-micropython.herokuapp.com/, where people chat in real time.
