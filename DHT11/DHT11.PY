import board
import adafruit_dht
import time

# Set sensor type : Options are DHT11,DHT22 or AM2302
sensor = adafruit_dht.DHT11(board.D13)

while True:
    try:
        # Use the 'temperature' and 'humidity' properties of the sensor object
        temperature = sensor.temperature
        humidity = sensor.humidity

        # Print the temperature and humidity values to the console
        print(f"Temperature: {temperature:.1f}°C\t Humidity: {humidity}%")

    except RuntimeError as error:
        # Reading the DHT11 sensor may result in occasional errors,
        # so we'll print the error message if this happens.
        print(f"Failed to read sensor data: {error.args[0]}")

    # Wait for 2 seconds before reading the sensor again
    time.sleep(2)