# LightBoard

The Light Board is run by a microcomputer called a Raspberry Pi.


### Using the Light Board
Lightboard & Raspberry Pi Resources / Notes

Login UserName: pi
Login Password: techstudents

Set the Date and Time via terminal (needed to connect to internet).

`sudo date -s "2023-11-28 11:06:00"`

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


