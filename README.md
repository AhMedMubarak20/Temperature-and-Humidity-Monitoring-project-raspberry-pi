# Temperature-and-Humidity-Monitoring-project-raspberry-pi
Creating a temperature and humidity monitoring project using a Raspberry Pi can be a fun and practical DIY project. In this project, we'll use a DHT11 or DHT22 sensor to measure temperature and humidity, and we'll write a Python script to display and log this data. Here are the steps to get you started:

Components Needed:

Raspberry Pi (any model with GPIO pins)
DHT11 or DHT22 sensor (DHT22 is more accurate)
Breadboard and jumper wires
10k ohm resistor (for DHT22)
MicroSD card with Raspbian OS installed
Power supply for the Raspberry Pi
Hardware Setup:

Connect the DHT11 or DHT22 sensor to the Raspberry Pi as follows:

VCC (3.3V) -> Pin 1 (3.3V)
Data -> Pin 7 (GPIO4)
GND -> Pin 6 (GND)
For DHT22, connect a 10k ohm resistor between VCC and Data.
Make sure your Raspberry Pi is powered off, then insert the MicroSD card with Raspbian OS installed.

Power up your Raspberry Pi.

Software Setup:

Open a terminal on your Raspberry Pi or SSH into it from another computer.

Update your system by running the following commands:

bash:
sudo apt update
sudo apt upgrade
Install the required Python libraries for the DHT sensor:

For DHT11:

bash:
sudo pip3 install adafruit-circuitpython-dht
For DHT22:

bash:
sudo pip3 install Adafruit_DHT
Create a Python script for reading and logging temperature and humidity data. Create a file, e.g., temp_humidity_monitor.py, and add the following code:

python Code.

Save and run the script:

bash:
python3 temp_humidity_monitor.py
This script will continuously read and display the temperature and humidity data every 10 seconds.

Optional Enhancements:

Log the data to a file or a database for historical tracking.
Set up a web server on your Raspberry Pi to display the data remotely.
Use external services like ThingSpeak or Adafruit IO to store and visualize your data.
Add a display (such as an OLED screen) to show the data locally.
