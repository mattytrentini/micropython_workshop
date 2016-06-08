Development Board
*****************

The board we are using is called "NodeMCU AMICA" and has an ESP8266 module
on it, which we will be programming. It comes with the latest version of
Micropython already setup on it, together with all the drivers we are going
to use.

.. note::
    The D0, D1, D2, ... numbers printed on the board are different from what
    Micropython uses -- because originally those boards were made for a
    different software. Make sure to refer to the image below to determine
    which pins are which.

.. image:: ./images/board.png
    :width: 512px


On top it has a micro-USB socket, for connecting to the computer. Next to it
are two buttons, one for reset and one for flashing. Then on both sides of the
board are two rows of pins, to which we will be connecting cables.

The symbols meaning is as follows:

  * ``3v3`` - this is a fancy way to write 3.3V, which is the voltage that the
    board runs on internally. You can think about this pin like the plus side
    of a battery. There are several pins like this, they are all connected
    inside.
  * ``gnd`` - this is the ground. Think about it like the minus side of the
    battery. They are also all connected.
  * ``gpioXX`` - "gpio" stands for "general purpose input output". Those are
    the pins we will be using for sending and receiving signals to and from
    various devices that we will connect to them. They can act as output --
    pretty much like a switch that you can connect to plus or to minus with
    your program.  Or they can act as input, telling your program whether they
    are connected to plus or minus.
  * ``a0`` - this is the analog pin. It can measure the voltage that is applied
    to it, but it can only handle up to 1V.
  * ``vin`` - this pin is connected with the 5V from your computer. You can
    also use it to power your board with a battery when it's not connected to
    the computer. The voltage applied here will be internally converted to the
    3.3V that the board needs.
  * ``rst`` - this is a reset button (and a corresponding pin, to which you can
    connect external button).
  * ``flash`` - hold down this button while resetting to bring the board into
    programming mode (also known as flashing mode).

The other pins are used internally by the board, and we will not be connecting
anything to them.

