Getting Started
***************

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
