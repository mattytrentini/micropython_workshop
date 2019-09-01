# This file is executed on every boot (including wake-boot from deepsleep)

# Stuff that came with MicroPython
#import esp
#esp.osdebug(None)
import uos, machine
#uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
#import webrepl
#webrepl.start()
gc.collect()

# Default to RGB LED shield being disabled (if connected)
import wemos, neopixel, machine
np = neopixel.NeoPixel(machine.Pin(wemos.D4), 7)
np.fill((0,0,0))
np.write()
del(np)
gc.collect()
