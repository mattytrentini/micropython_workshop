Getting Started
***************

This section describes how to start utilising some of the MicroPython specific
features of your board by itself, before we start adding more hardware into the
mix in the coming pages.

LED Basics
==========

The traditional first program for hobby electronics is a blinking light - so
let's stick with tradition and try to build that!

The boards you have actually have an LED built-in, so we can use that. It
actually has three in fact - a red "power" LED, a blue "battery charge" LED,
and a green LED that we can control (it defaults to off so it may not be easy
to find until you enable it!).

One side of the green LED is connected to the ``GND`` (0 volts) pin internally,
and the other side is connected to ``D1``. We should be able to make that LED
shine with our program by making ``D1`` behave like the ``3V3`` (3.3 volt)
pins. We need to "set the ``D1`` pin high", or in other words, make it
connected to ``3V3``. Let's try that::

    from machine import Pin
    import d1_mini

    led = Pin(d1_mini.LED, Pin.OUT)
    led.on()

The first line "imports" the "Pin" function from the "machine" module. In
Python, to use any libraries, you first have to import them. The "machine"
module contains most of the hardware-specific functions in Micropython.

The second line imports a helper "d1_mini" module that provides the pin
mappings to easily interact with specific pins on the board. Note that that is
the number one after the letter ``d``, not a lower case L!
Each of the digital pins (``Dx``) on the board can be found in this module, as
well as some hardware-role-specific pins (such as those used for :ref:`I2C` or
`SPI`_ communications). Note that this module is specifically for D1 Mini form
factor boards, such as the Wemos D1 Mini and the TTGO MINI 32 - if you were to
use a different board, you would likely need a different helper module!

.. _SPI: https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi/all

Once we have the "Pin" function imported, we use it to create a pin object,
with the first parameter telling it to use the ``LED`` value from our helper
module, and the second parameter telling it to switch it into output mode
(instead of the input mode it would default to otherwise). Once
created, the pin is assigned to the variable we called "led".

Finally, we set the pin high, by calling the "on" method on the "led"
variable. At this point the LED should start shining - exciting!

Now, how to make the LED stop shining? There are two ways. We could switch it
back into "input" mode, where the pin is not connected to anything. Or we could
turn the microcontroller pin "off". If we do that, both ends of the LED will be
connected to ``GND``, and the current won't flow. We do that with::

    led.off()


LED Blinking
============

Now, how can we make the LED blink 10 times? We could of course type
``led.on()`` and ``led.off()`` ten times quickly, but that's a lot of work
and we have computers to do that for us. We can repeat a command or a set of
commands using the "for" loop::

    for i in range(10):
        led.on()
        led.off()

What happened? Nothing interesting, the LED just shines like it did. That's
because the program blinked that LED as fast as it could -- so fast, that we
didn't even see it. We need to make it wait a little before the blinks, and for
that we are going to use the "time" module. First we need to import it::

    import time

And then we will repeat our program, but with the waiting included::

    for i in range(10):
        led.on()
        time.sleep(0.5)
        led.off()
        time.sleep(0.5)

Now the LED should turn on and off every half second!


Networking
==========

One of the exciting features of the ESP32 microcontroller (the heart of the
TTGO MINI 32) is built-in Wi-Fi. While Wi-Fi itself may be a complicated
beast, luckily for us MicroPython makes it simple to use! First of all lets
connect to the network::

    import network
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect('<your SSID>', '<your password>')

You will have to replace ``<your SSID>`` and ``<your password>`` with the
relevant login details for your network.

This creates a reference to the STAtion InterFace of the board (type of
Wi-Fi connection that connects to an Access Point), enables it, and then
attempts to connect to the defined network. The success of this can be checked
with::

    sta_if.isconnected()

Once a connection is established, the details of this can be checked with::

    sta_if.ifconfig()

Which provides the device IP, device netmask, default gateway, and DNS server.

More network control commands can be found in the
`MicroPython WLAN documentation`_. There is also an Access Point interface
(``network.AP_IF``) which allows other devices to connect to your device. This
can be very useful, but for the moment we're just going to focus on connecting
to another network - as this allows us to reach out to harness the power of the
internet!

.. _`MicroPython WLAN documentation`: http://docs.micropython.org/en/latest/library/network.WLAN.html

.. _`Internet Requests`:

This Jen, is The Internet
=========================

Now that we've got a network connection (and that network extends out to the
World Wide Web), it's a relatively simple matter to make web requests,
utilising the ``urequests`` library. This is a MicroPython implementation of
the `Python requests library`_. It's had some features gutted to make it more
microcontroller friendly, but it is still powerful!

.. _`Python requests library`: https://2.python-requests.org/en/master/

To test it out, lets retrieve a random activity from the `Bored API`_::

    import urequests
    req = urequests.get('https://www.boredapi.com/api/activity/')

.. _`Bored API`: https://www.boredapi.com/

And with that, we should now have the response to our activity request request!
The text of the response can be found in ``req.text`` -- check it out!

This is a `JSON`_ API, and so we can see the text of our request result is a
string encoded JSON response. Turning a JSON string into a Python ``dict`` is
pretty easy in Python (and MicroPython), and even easier when dealing with a
request, as we can simply call the ``.json()`` method on it::

    >>> req_dict = req.json()
    >>> print(req_dict['activity'])
    'Make homemade ice cream'

.. _`JSON`: https://www.json.org/

As simply as that, we can now harness information from the internet, and the
myriad of public APIs out there (like those on `this list of public APIs`_ I
found). Not only that, by using `query strings`_ we can pass information to
websites, either for storage or for a customised response. We also have access
to PUT requests, not just GET requests. I won't go into that here, but be aware
that it is a simple thing to do if you need to!

.. _`this list of public APIs`: https://github.com/public-apis/public-apis
.. _`query strings`: https://en.wikipedia.org/wiki/Query_string

Now that we've got the basic functions of the board under control, lets get
some more hardware involved!
