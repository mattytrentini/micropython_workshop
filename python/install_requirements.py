import pyboard
import sys

COMMAND, PORT = sys.argv[1:3]

pyb = pyboard.Pyboard(PORT)
pyb.enter_raw_repl()

result = 0

if COMMAND == "INSTALL":
    SSID, PWRD = sys.argv[3:5]
    out = pyb.exec("""
import network, upip
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('%s', '%s')
while not sta_if.isconnected(): pass
upip.install('uasyncio')
""" % (SSID, PWRD))
    print(out)
elif COMMAND == "TEST":
    out = pyb.exec("""
try:
    import d1_mini
    import uasyncio
    import tm1640
    import max7219
    import ssd1306
except Exception as e:
    print('Test failed, %s: %s' % (e.__class__.__name__, str(e)))
else:
    print('Test successful!')
    """)
    print(out)
    if b'Test successful!' not in out:
        result = -1

pyb.exit_raw_repl()
result
