Getting Started
***************

This section describes how to start utilising some of the MicroPython specific
features of your board by itself, before we start adding more hardware into the
mix in the coming pages.

LED Basics
==========

The traditional first program for hobby electronics is a blinking light. We
will try to build that.

The boards you have actually have a light built-in, so we can use that. There
is an LED (light-emitting diode) near the centre of the board. The plus
side of that LED is connected to the ``3v3`` pins internally, and the minus
side is connected to ``D4``. So we should be able to make that LED shine with
our program by making ``D4`` behave like the ``gnd`` pins. We need to "bring
the ``D4`` pin low", or in other words, make it connected to ``gnd``. Let's try
that::

    from machine import Pin
    import wemos

    led = Pin(wemos.LED, Pin.OUT)
    led.off()

The first line "imports" the "Pin" function from the "machine" module. In
Python, to use any libraries, you first have to import them. The "machine"
module contains most of the hardware-specific functions in Micropython.

The second line imports a helper "wemos" module that provides the pin
mappings to easily interact with specific pins on the board. Each of the
digital pins (``Dx``) on the board can be found in this module, as well as
some hardware-role-specific pins (such as those used for `I2C`_ or `SPI`_
communications). Note that this module is specifically for the Wemos D1 Mini -
if you were to use a different board, you would likely need a different helper
module!

.. _I2C: https://learn.sparkfun.com/tutorials/i2c/all
.. _SPI: https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi/all

Once we have the "Pin" function imported, we use it to create a pin object,
with the first parameter telling it to use the ``LED`` value from our helper
module, and the second parameter telling it to switch it into output mode
(instead of the input mode it would default to otherwise). Once
created, the pin is assigned to the variable we called "led". ``D4`` is also
connected to the LED, and can also be found in the ``wemos`` module - you can
see that they're the same by running ``wemos.LED == wemos.D4`` in the REPL.

Finally, we bring the pin low, by calling the "off" method on the "led"
variable. At this point the LED should start shining. It may seem confusing
that turning the "LED" off makes the light turn on, but what we need to
remember is that we're not controlling the LED (at least not directly) - we're
controlling the microcontroller pin. The microcontroller pin is turning off
(getting set to zero volts) - but due to the circuitry this means that the LED
is enabled.

Now, how to make the LED stop shining? There are two ways. We could switch it
back into "input" mode, where the pin is not connected to anything. Or we could
turn the microcontroller pin "on". If we do that, both ends of the LED will be
connected to ``3v3``, and the current won't flow. We do that with::

    led.on()


LED Blinking
============

Now, how can we make the LED blink 10 times? We could of course type
``led.off()`` and ``led.on()`` ten times quickly, but that's a lot of work
and we have computers to do that for us. We can repeat a command or a set of
commands using the "for" loop::

    for i in range(10):
        led.on()
        led.off()

Note, that when you are typing this, it will look more like::

    >>> for i in range(10):
    ...     led.on()
    ...     led.off()
    ...
    ...
    >>>

That's because the REPL automatically understands that when you indent a
line, you mean it to be a block of code inside the "for" loop. You have to
un-indent the last line (by removing the spaces with backspace) to finish this
command. You can avoid that by using "paste mode" -- press ``ctrl+E``, paste
your code, and then press ``ctrl+D`` to have it executed.

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

One of the exciting features of the ESP8266 microcontroller (the heart of the
WEMOS D1 Mini board) is built-in Wi-Fi. While Wi-Fi itself may be a complicated
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