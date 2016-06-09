Advanced
********


Schematics
==========

The pretty colorful pictures that we have been using so far are not very
useful in practical projects. You can't really draw them by hand, different
components may look very similar, and it's hard to see what is going on when
there are a lot of connections. That's why engineers prefer to use more
symbolic representation of connection, a schematic.

A schematic doesn't care how the parts actually look like, or how their pins
are arranged. Instead they use simple symbols. For instance, here's a schematic
of our experiment with the external LED:

.. image:: ./images/blink_schem.png

The resistor is symbolized by a zig-zag. The LED is marked by a diode symbol
(a triangle with a bar), with additional two arrows showing that it's a light
emitting diode. The board itself doesn't have a special symbol -- instead it's
symbolized by a rectangle with the board's name written in it.

There is also a symbol for "ground" -- the three horizontal lines. Since a lot
of components need to be usually connected to the ground, instead of drawing
all those wires, it's easier to simply use that symbol.

Here are some more symbols:

.. image:: ./images/schematic.png

It's important to learn to read and draw electric schematics, because anything
more advanced is going to use them, and you will also need them when asking for
help on the Internet.
