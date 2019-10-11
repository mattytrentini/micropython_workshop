LED Matrix Shield
*****************

.. highlight:: python
   :linenothreshold: 4

.. figure:: /images/matrix_shield_top.png
   :width: 270

   LED Matrix Shield

The LED Matrix Shield allows us to control an 8x8 red LED matrix. Each LED in
the matrix is controllable so small icons can be display or, more commonly,
letters. With a little bit of clever programming we can update the matrix
quickly and scroll text on it!

Plug in to the matrix
=====================

Insert the LED Matrix Shield into the Microcontroller board taking
care to orient the board correctly - align the Wemos logo on the shield at
the USB socket end of the Microcontroller board:

.. figure:: /images/matrix_shield_plugged_in.png
   :width: 270

Technical details
=================

Controlling all the LEDs is an *LED driver* known as the `TM1640`_ - you can
see it on the underside of the LED Matrix Shield:

.. figure:: /images/matrix_shield_bottom.png
   :width: 270

   The large *integrated circuit* is the TM1640


We can use the Microcontroller to tell the TM1640 which LEDs to turn on
and off. The TM1640 expects you to speak it's *protocol* that needs two
signals - *CLOCK* and *DATA* to be manipulated in just the right way.

.. NOTE::
    *CLOCK* is connected to the pin labelled **D5** and *Data* is
    connected to **D7**.

Thankfully we have software that implements this protocol, making it *much*
easier to specify which LEDs to turn on or off. Let's get to it!

.. _TM1640: https://cdn.solarbotics.com/products/datasheets/tm1640.pdf

X marks the spot
================
Make a connection to your microcontroller and enter the following code::

    import tm1640
    import wemos
    tm = tm1640.TM1640(clk=wemos.D5, dio=wemos.D7)
    tm.text('X')

If everything worked you should see an X on the LED matrix!

.. figure:: /images/led_matrix_x.png

Looking into the code, we start by importing the required libraries; ``tm1640``
is the module that allows the microcontroller to talk with the TM1640 LED
driver. ``wemos`` contains our Pin definitions.

Then we simply construct our TM1640 object and configure which pins are used.
Finally we *render* an X to the matrix by calling ``.text()``.

What else can we do with the ``tm1640`` module? We can *scroll* text::

    import tm1640
    import wemos
    tm = tm1640.TM1640(clk=wemos.D5, dio=wemos.D7)
    tm.scroll('MicroPython is easy!')

