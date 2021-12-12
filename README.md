# Setup

This is a little project I built for Christmas: a remote-controlled LED-illuminated star. 

## Wiring

The wiring is pretty easy. TODO add the diagrams...

## Setup the Raspberry Pi

First, we have to set up the Raspberry Pi.

1. Download the [Raspberry Pi imager](https://www.raspberrypi.com/software/) and write your image to the SD card (Lite image works fine)
2. Enable ssh and WiFi
    1. Create the `ssh` file in the boot partition
    2. Create and configure the `wpa_supplicant.conf` file in the boot partition so the Raspberry can connect to WiFi
3. Start up your Pi and try to login via ssh

Sometimes, you might have to [enable SPI](https://www.raspberrypi-spy.co.uk/2014/08/enabling-the-spi-interface-on-the-raspberry-pi/).

## Run the Webserver

The server uses [pipenv](https://pipenv.pypa.io/en/latest/) to manage the Python dependencies.

1. `pip3 install --user pipenv`
2. Add the pipenv installation directory to PATH if necessary (a message will show the binary's location after the installation)
3. Clone the [repository](https://github.com/moredatapls/raspberry-christmas-star) and change into the directory
4. Install the dependencies: `CFLAGS="-fcommon" pipenv install` (the CFLAGS were needed in my case, see [here](https://forum.manjaro.org/t/pip-install-rpi-gpio-fail/25788/4))
5. After the installation, run the server (GPIO requires root privileges): `sudo -E env PATH=$PATH pipenv run python main.py`

## Setup system.d

We'll use systemd to automatically run the service in the background (and to run it after the Raspberry boots up).

1. Copy the [star.service file](rpi-config/star.service) to `/etc/systemd/service/` and replace `<TODO>` with the path to the repo that you cloned
2. Run `sudo systemctl start start` to start the service
3. Run `sudo systemctl enable star` to run the service after boot
