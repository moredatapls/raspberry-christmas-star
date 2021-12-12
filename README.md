# Setup

## Raspberry Pi

1. Download the Raspberry Pi imager and write your image to the SD card (Lite image works fine)
2. Enable ssh and WiFi
    1. Create the `ssh` file in the boot partition
    2. Create and configure the `wpa_supplicant.conf` file in the boot partition
3. Start up your Pi and try to login via ssh

enable spi https://www.raspberrypi-spy.co.uk/2014/08/enabling-the-spi-interface-on-the-raspberry-pi/

run locally:

sudo pip install pipenv
sudo su
CFLAGS="-fcommon" pipenv install

1. `pip3 install --user pipenv`
2. add dir to PATH if necessary
3. change to the project root dir
4. run `CFLAGS="-fcommon" pipenv install` [1](https://forum.manjaro.org/t/pip-install-rpi-gpio-fail/25788/4)
5. run with sudo (gpio requires that): `sudo -E env PATH=$PATH pipenv run python main.py`


maybe:

sudo pip3 uninstall rpi_ws281x
sudo pip3 install rpi_ws281x
