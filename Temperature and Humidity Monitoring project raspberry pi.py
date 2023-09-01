import Adafruit_DHT
import time

sensor = Adafruit_DHT.DHT22  # Change to DHT11 if using DHT11
pin = 4  # GPIO pin where the data line is connected

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        print(f'Temperature: {temperature:.2f}°C, Humidity: {humidity:.2f}%')
        # You can add code here to log the data to a file or send it to a cloud service.
    else:
        print('Failed to retrieve data. Try again later.')
    time.sleep(10)  # Read data every 10 seconds
