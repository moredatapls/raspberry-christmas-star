#!/bin/bash

# https://github.com/jgarff/rpi_ws281x/issues/294
sudo apt install -y\
	gcc \
	git \
	python3-pip \
	libzbar-dev \
	libzbar0 \
	libffi-dev \
	clang \
	python3-dev \
	libssl-dev \
	build-essential

sudo pip3 install pyparsing==2.1.0 pyparser==1.0

sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel
sudo python3 -m pip install --force-reinstall adafruit-blinka
