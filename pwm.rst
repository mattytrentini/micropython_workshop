Pulse Width Modulation
**********************

Wouldn't it be neat if instead of blinking, the LED slowly became brighter and
then fade out again? Can we do this somehow?

The brightness of the LED depends on the voltage being supplied to it.
Unfortunately, our GPIO pins only have a simple switch functionality -- we
can turn them on or off, but we can't fluently change the voltage (there are
pins that could do that, called DAC, for "digital to analog converter", but
our board doesn't have those). But there is another way. Remember when we
first tried to blink the LED without any delay, and it happened too fast to
see?

Turns out we can blink the LED very fast, and by varying the time it is on and
off change how bright it seems to be to the human eye. The longer it is on and
the shorter it is off, the brighter it will seem.

Now, we could do that with a simple loop and some very small delays, but it
would keep our board busy and prevent it from doing anything else, and also
wouldn't be very accurate or terribly fast. But the ESP8266 has special
hardware dedicated just for blinking, and we can use that! This hardware is
called PWM (for Pulse Width Modulation), and you can use it like this::

    from machine import Pin, PWM
    import time

    pwm = PWM(Pin(2))
    pwm.duty(896)
    time.sleep(1)
    pwm.duty(512)
    time.sleep(1)
    pwm.duty(0)

If you run this, you should see the blue led on ``gpio2`` change brightness.
The possible range is from 1023 (100% duty cycle, the LED is off) to 0 (0%
duty cycle, the LED is on full brightness). Why is 0 full brightness? Remember,
that the LED on the ``gpio2`` is reversed -- it shines when the pin is off,
and the duty cycle tells how much the pin is on.

You can also change the frequency of the blinking. Try this::

    pwm.freq(1)

That should blink the LED with frequency of 1Hz, so once per second -- we are
basically back to our initial program, except the LED blinks "in the
background" controlled by dedicated hardware, while your program can do other
things!
