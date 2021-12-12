<h1 align="center">
   <img style="width: 70%" src="https://raw.githubusercontent.com/moredatapls/raspberry-christmas-star/master/img/banner.jpg" />
   
   Raspberry Pi Christmas Star
</h1>

This is a little project I built for Christmas: a remote-controlled LED-illuminated star that I can hang on my window.
The star is controlled by a Raspberry Pi Zero. It is illuminated by a Neopixel LED strip.

To control the star from any service in your network, the Raspberry Pi runs a little Python-based webserver (Flask).
It serves a static website with a color wheel ([Iro.js](https://iro.js.org/)). By moving the color wheel you can
change the color of the star.

## Parts

* Raspberry Pi Zero
* Neopixel LED Strip
* 5V power supply

TODO complete the parts list...

## Wiring

The wiring is pretty easy. Instead of powering the Raspberry Pi through MicroUSB, I am powering it through the GPIO pins, which makes the wiring
a bit easier.

TODO complete the diagrams...

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
