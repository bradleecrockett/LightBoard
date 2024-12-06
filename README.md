# LightBoard

The Light Board is run by a microcomputer called a Raspberry Pi.
Set the Date and Time via terminal (needed to connect to internet).

`sudo date -s "2023-11-28 11:06:00"`


### Using the Light Board

* Our lightstrip is a ws2812 leds 12Volt (power) Power must be supplied from a large power supply. Do not attempt to poser the LED Board without the powersupply from the Raspberry Pi.
* Data is pin 12 (6th from corner) aka GPIO18
* Ground is pin 20 (7th from corner) many more GNDs available (6, 9, 14, 20, 25, 30, 34, 39). This needs to share a ground with the power supply as well.
 ![GPPI DIagram](GPIO.png)
    


Basic Setup:
https://youtu.be/KJupt2LIjp4 

This will not get us connected wirelessly over the internet but it will allow us to write code directly on the RPI and test the light board. We followed this tutorial to hookup the board.  I have soldered some wire connections so that it should be pretty easy to hook up.  



## Using a virtual environment venv 
https://www.raspberrypi.com/documentation/computers/os.html#python-on-raspberry-pi

## Imports / software install
```
pip install rpi_ws281x
pip install adafruit-circuitpython-neopixel
```


### Use Thonny to write code. (SAVE)
To run the code on the light board
`sudo python3 file_name.py`



	
### To connect via ssh
Both computers must be connected to the same network. (Roseville Cemetary)

```
ssh userName@ip_address
ssh pi@192.268.1.90
```


### Wireless transfer over ssh:
https://howtoraspberrypi.com/transfer-files-raspberry-ssh/

To change directories

`cd new_directory`


