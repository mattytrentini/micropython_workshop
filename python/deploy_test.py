import pyboard
import sys

PORT = sys.argv[1]

pyb = pyboard.Pyboard(PORT)
pyb.enter_raw_repl()

result = 0
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
