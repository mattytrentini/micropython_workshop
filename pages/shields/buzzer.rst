Buzzer Shield
*************

.. highlight:: python
   :linenothreshold: 4

.. figure:: /images/buzzer_shield_top.png
   :width: 270

The Buzzer Shield is a Wemos D1 Mini shield, featuring a buzzer which can be
used for generating sounds.

The buzzer is controlled by simply toggling the appropriate pin at the specific
frequency that we want to hear. We could do this by repeatedly setting our pin
high, waiting for a period, and then setting it low again, however this would
be very laborious. Instead, we're going to use a technique called
`Pulse-Width Modulation`_, (PWM). This is a feature of our hardware (so it's
very fast and stable, instead of relying on a software implementation), and
we can set it up and control it using the `MicroPython PWM function`_.

.. _`Pulse-Width Modulation`: https://en.wikipedia.org/wiki/Pulse-width_modulation
.. _`MicroPython PWM function`: https://docs.micropython.org/en/latest/esp8266/tutorial/pwm.html

Make Some Noise
===============

In order to start working with the buzzer, we'll need to connect the shield
to the Wemos D1 Mini board itself. If there is already a shield connected to
your board (such as the LED Matrix shield from the previous section), then
first remove this. Then plug the buzzer shield into the board -- the large,
black component (the buzzer!) should be over the USB port of the main board.
Then simply align the 8 pins on either side with the sockets on the main board
and push them together!

.. figure:: /images/buzzer_shield_connected.png

   Note the large black component over the USB connection

Now we've got the shield on the board, connect to the board with your USB
again, and get into Mu. Now before we start using the buzzer...

.. WARNING::
   When we use the buzzer, we tell it to produce a set frequency - it will keep
   doing this indefinitely until we tell it to stop (or you unplug it)! This
   may be loud / unintended -- as such, always make sure you know how to
   disable the buzzer (will be in the code below), and where possible have your
   scripts copy + pasted in or running from a file (instead of typing the
   commands into the REPL) with a the buzzer disabling at the end of the script
   (after a delay) so that we're only getting sounds when we want them!

Now that we've got that out of the way, lets make some noise::

    import machine
    import wemos
    import time
    buzzer_pin = machine.Pin(wemos.D6, machine.Pin.OUT)
    buzzer = machine.PWM(buzzer_pin)
    buzzer.freq(1000)
    buzzer.duty(10)
    time.sleep(1)
    buzzer.duty(0)

If all went well, your buzzer should have made a (1 kHz) beep for 1 second, and
then stopped! Now lets run through what we just did:

- Imported the MicroPython ``machine`` module -- we need this to configure our
  pin to control the buzzer
- Imported our ``wemos`` module -- we need this to get the pin information to
  then configure the correct pin to use for the buzzer
- Imported the MicroPython ``time`` module -- we're going to use this to add
  delays to the code
- Created an object that controls pin connected to the buzzer, and set it as an
  output (as we will be `driving` the buzzer)
- Created a new object that gives us PWM control over the buzzer pin
- Set the PWM frequency to 1000 herts, or 1kHz -- note that this does not
  generate any noise by itself, as the PWM defaults to having a duty cycle of 0
  (that is, it is enabled 0% of each cycle)
- Set the PWM duty cycle to 10 -- the duty cycle is a 10 bit number (has a
  maximum of 1023) so by setting it to 10, it will be enabled roughly 1% of
  the time. This is what makes it buzz!
- Delays code execution by 1 second -- this gives us an opportunity to hear it
  buzzing
- Sets the PWM duty cycle to 0 -- stops the buzzer producing any noise (as it
  is once again enabled 0% of the time)

A couple of the numbers in here may seem a tad arbitrary, so lets explain them
a bit better.

We used a frequency of 1000 because the buzzer has a peak frequency response
between 1 and 3 kHz -- this is the area where it provides the best results.
It will still work outside this range however!

We used a duty cycle of 10 to reduce the volume of the sound output. Peak
volume is at 50% duty cycle (setting of ~512), however due to the
logarithmic nature of sound, we only need a small amount of this to make a
relatively loud buzz. Because the buzzer generates sounds by alternating the
voltage over the diaphragm, moving closer to 100% duty cycle has the same
effect as being close to 0% duty cycle. Feel free to try buzzing at 50% duty
cycle to see why we reduced the output!

Being able to make `a` sound is nice, but it would be even nicer to make a
`nice` sound. First of all, lets define the frequencies of some specific
notes::

    C4  = 262
    CS4 = 277
    D4  = 294
    DS4 = 311
    E4  = 330
    F4  = 349
    FS4 = 370
    G4  = 392
    GS4 = 415
    A4  = 440
    AS4 = 466
    B4  = 494
    C5  = 523
    CS5 = 554
    D5  = 587
    DS5 = 622
    E5  = 659
    F5  = 698
    FS5 = 740
    G5  = 784
    GS5 = 831
    A5  = 880
    AS5 = 932
    B5  = 988

These are taken from the `Pyboard "Play Tone" page`_ -- you will see that there
are more notes on that page. We're not defining the lower range as two
octaves will serve us fine, and we're not defining any higher notes because we
can't use them! Unfortunately the maximum PWM frequency on the ESP8266 (the
microcontroller that is running on our Wemos D1 Mini) is 1 kHz. If we upgraded
to an `ESP32`_ based board (the next microcontroller in the family) then we
wouldn't have this limitation, but it would cost a bit more.

.. _`Pyboard "Play Tone" page`: http://wiki.micropython.org/Play-Tone
.. _`ESP32`: https://www.espressif.com/en/products/hardware/esp32/overview

Now lets create a function that will allow us to play a song by passing it a
buzzer object, a list of notes, the delay between each note, and an optional
duty cycle to use when playing a note::

    def play(buz, notes, delay, active_duty=10):
        for note in notes:
            if note == 0:  # Special case for silence
                buz.duty(0)
            else:
                buz.freq(note)
                buz.duty(active_duty)
            time.sleep(delay)
        buz.duty(0)

To put it into action, lets create a song by defining a list of notes, and then
``play()`` it::

    song = [
         E5, E5,  0, E5,  0, C5, E5,  0,
         G5,  0,  0,  0, G4,  0,  0,  0,
         C5,  0,  0, G4,  0,  0, E4,  0,
          0, A4,  0, B4,  0,AS4, A4,  0,
         G4, E5,  0, G5, A5,  0, F5, G5,
          0, E5,  0, C5, D5, B4,  0,  0,
         C5,  0,  0, G4,  0,  0, E4,  0,
          0, A4,  0, B4,  0,AS4, A4,  0,
         G4, E5,  0, G5, A5,  0, F5, G5,
          0, E5,  0, C5, D5, B4,  0,  0,
    ]
    play(buzzer, song, 0.15)

With any luck we should have heard a recognisable little tune! We've now set
up a framework to allow us to play arbitrary songs -- neat!

Exercises
=========

Time to take those concepts and put them into action! The following subsections
detail different exercises that can be accomplished using the techniques
covered so far.

Alerts
------

Set up a ``success()`` function that you could easily put into a future project
that utilises the buzzer to play a success notification (the audio equivalent
of a green tick). What that sounds like is up to your imagination!

Extension: Make a ``failure()`` function for when things don't quite go as
planned.
