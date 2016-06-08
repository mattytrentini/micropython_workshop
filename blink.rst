Blink
*****

The traditional first program for hobby electronics is a blinking light. We
will try to build that.

The boards you have actually have a light built-in, so we can use that. There
is a LED (light-emitting diode) near the antenna (the golden zig-zag). The plus
side of that LED is connected to the ``3v3`` pins internally, and the minus
side is connected to ``gpio2``. So we should be able to make that LED shine
with our program by making ``gpio2`` behave like the gnd pins. We need to
"bring the ``gpio2`` low", or in other words, make it connected to ``gnd``.
Let's try that::

    from machine import Pin

    led = Pin(2, Pin.OUT)
    led.low()

The first line "imports" the "Pin" function from the "machine" module. In
Python, to use any libraries, you first have to import them. The "machine"
module contains most of the hardware-specific functions in Micropython.

Once we have the "Pin" function imported, we use it to create a pin object,
with the first parameter telling it to use ``gpio2``, and the second parameter
telling it to switch it into output mode. Once created, the pin is assigned to
the variable we called "led".

Finally, we bring the pin low, by calling the "low" method on the "led"
variable. At this point the LED should start shining. In fact, it may have
started shining a line earlier, because once we switched the pin into output
mode, its default state is "low".

Now, how to make the LED stop shining? There are two ways. We could switch it
back into "input" mode, where the pin is not connected to anything. Or we could
bring it "high". If we do that, both ends of the LED will be connected to
"plus", and the current won't flow. We do that with::

    led.high()

Now, how can we make the LED blink 10 times? We could of course type
``led.low()`` and ``led.high()`` ten times quickly, but that's a lot of work
and we have computers to do that for us. We can repeat a command or a set of
commands using the "for" loop::

    for i in range(10):
        led.high()
        led.low()

Note, that when you are typing this, it will look more like::

    >>> for i in range(10):
    ...     led.high()
    ...     led.low()
    ...
    ...
    >>>

That's because the console automatically understands that when you indent a
line, you mean it to be a block of code inside the "for" loop. You have to
un-indent the last line (by removing the spaces with backspace) to finish this
command.

What happened? Nothing interesting, the LED just shines like it did. That's
because the program blinked that LED as fast as it could -- so fast, that we
didn't even see it. We need to make it wait a little before the blinks, and for
that we are going to use the "time" module. First we need to import it::

    import time

And then we will repeat our program, but with the waiting included::

    for i in range(10):
        led.high()
        time.sleep(0.5)
        led.low()
        time.sleep(0.5)

Now the LED should turn on and off every half second.
