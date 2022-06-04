# rpi-plant-project
An automatic plant watering system created with Python and a Raspberry Pi.

You can read more about how I created this project [here](https://dev.to/alanjc/water-your-plant-using-a-raspberry-pi-and-python-2ddb).

<img src="https://raw.githubusercontent.com/AlanConstantino/personal-blog/master/images/rpi-plant-article/complete-water-pump.jpg">

# Dependencies
- [gpiozero library](https://gpiozero.readthedocs.io/en/stable/index.html)
  - Used for interfacing with the GPIO pins on the Raspberry Pi
- [schedule api](https://schedule.readthedocs.io/en/stable/)
  - Used for running Python functions at pre-determined intervals
- [smtplib module](https://docs.python.org/3/library/smtplib.html)
  - Used for sending emails
- [ssl module](https://docs.python.org/3/library/ssl.html)
  - Used in tandem with the smtplib module
  
# Installing
The gpiozero library should already be installed into your Pi by default but if not you can run the following command:

<code>sudo pip3 install gpiozero</code>

You can install the schedule api by running the following command:

<code>sudo pip3 install schedule</code>

To install this code onto your Raspberry Pi you can clone the repository to your Pi's Desktop by typing in the following command into the terminal:

<code>git clone https://github.com/AlanConstantino/rpi-plant-project.git</code>

Once cloned, you can move the "run" folder onto your Pi's desktop and then run the following command:

<code>sudo crontab -e</code>

Now you'll see a window that looks something like the following:

<img src="https://raw.githubusercontent.com/AlanConstantino/personal-blog/master/images/rpi-plant-article/pi-terminal.png">

From here, you want to append the following code snippet to the file:

<code>@reboot python3 /home/pi/Desktop/run/water_plant.py</code>

By doing so, you're telling the Pi "Hey whenever you reboot, run the python script 'water_plant.py' inside the 'run' folder located on our Desktop."

Now you can turn off your Pi and whenever you turn it back on, the "water_plant.py" script will get executed.
