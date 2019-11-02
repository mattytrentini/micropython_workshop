BIN ?= esp32-idf3-20190529-v1.11.bin
PORT ?= /dev/ttyS1
SSID ?= Useful_SSID
PWRD ?= Reasonable_Password

.PHONY: deploy reqs flash copy test 

deploy:	reqs flash copy test
	@echo Deployment complete!

reqs:
	pip3 show esptool || pip3 install esptool
	test -f pyboard.py || wget https://raw.githubusercontent.com/micropython/micropython/master/tools/pyboard.py
	test -f ssd1306.py || wget https://raw.githubusercontent.com/micropython/micropython/master/drivers/display/ssd1306.py

flash:
	test -f $(BIN) || wget https://micropython.org/resources/firmware/$(BIN)
	python3 -m esptool -p $(PORT) write_flash -z 0x1000 $(BIN)

copy:
	rshell -p $(PORT) cp max7219/max7219.py /pyboard
	rshell -p $(PORT) cp tm1640/tm1640.py /pyboard
	rshell -p $(PORT) cp ssd1306.py /pyboard
	@python3 install_requirements.py INSTALL $(PORT) $(SSID) $(PWRD)

test:
	python3 install_requirements.py TEST $(PORT)
