# Setup

## Raspberry Pi

1. Download the Raspberry Pi imager and write your image to the SD card (Lite image works fine)
2. Enable ssh and WiFi
    1. Create the `ssh` file in the boot partition
    2. Create and configure the `wpa_supplicant.conf` file in the boot partition
3. Start up your Pi and try to login via ssh

run locally:

1. `pip3 install --user pipenv`
2. add dir to PATH if necessary
3. change to the project root dir
4. run `CFLAGS="-fcommon" pipenv install` [1](https://forum.manjaro.org/t/pip-install-rpi-gpio-fail/25788/4)
5. run with sudo (gpio requires that): `sudo -E env PATH=$PATH pipenv run python main.py`

