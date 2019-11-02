BIN ?= esp32-idf3-20190529-v1.11.bin
PORT ?= /dev/ttyS3

.PHONY: deploy reqs flash erase copy test clean

deploy:	reqs flash copy test
	@echo Deployment complete!

reqs:
	pip3 show esptool || pip3 install esptool
	test -d uasyncio || (mkdir uasyncio && cd uasyncio \
		&& wget https://raw.githubusercontent.com/micropython/micropython-lib/master/uasyncio/uasyncio/__init__.py \
		&& wget https://raw.githubusercontent.com/micropython/micropython-lib/master/uasyncio.core/uasyncio/core.py \
		&& cd ..)
	test -f pyboard.py || wget https://raw.githubusercontent.com/micropython/micropython/master/tools/pyboard.py
	test -f ssd1306.py || wget https://raw.githubusercontent.com/micropython/micropython/master/drivers/display/ssd1306.py

flash:
	test -f $(BIN) || wget https://micropython.org/resources/firmware/$(BIN)
	python3 -m esptool -p $(PORT) write_flash -z 0x1000 $(BIN)

erase:
	python3 -m esptool -p $(PORT) erase_flash

copy:
	rshell -p $(PORT) mkdir /pyboard/lib
	rshell -p $(PORT) cp boot.py d1_mini.py /pyboard
	rshell -p $(PORT) cp -r uasyncio/ ssd1306.py max7219/max7219.py tm1640/tm1640.py /pyboard/lib

test:
	python3 install_requirements.py $(PORT)

clean:
	rm -rf uasyncio pyboard.py ssd1306.py