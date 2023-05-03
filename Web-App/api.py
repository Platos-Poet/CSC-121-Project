from flask import Flask, jsonify
import requests
from flask_cors import CORS
from IP import IP
from datetime import datetime

app = Flask(__name__)
cors = CORS(app)

OPENWEATHERMAP_API_KEY = "b2f82104ab9851dcf5b08eb56d3ede6a" # My personal API key

@app.route('/weather/<city>')
def get_weather(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHERMAP_API_KEY}&units=imperial'
    response = requests.get(url)
    if response.status_code == 200:
        # Creating the reponse returned
        weatherData = response.json()
        temperature = round(weatherData['main']['temp']) # convert temperature from Kelvin to Celsius
        humidity = weatherData['main']['humidity']
        windSpeed = weatherData['wind']['speed']
        weatherDescription = weatherData['weather'][0]['description'].title()
        pressure = weatherData['main']['pressure']
        sunrise = weatherData["sys"]["sunrise"]
        sunset = weatherData["sys"]["sunset"]
        sunrisedt = datetime.fromtimestamp(sunrise)
        sunriseT = sunrisedt.strftime("%I:%M:%S %p")
        sunsetdt = datetime.fromtimestamp(sunset)
        sunsetT = sunsetdt.strftime("%I:%M:%S %p")
        result = {
            'City': city,
            'Temperature': f"{temperature}°F",
            'Humidity': f"{humidity}%",
            'Wind Speed': f"{windSpeed} mph",
            'Weather Description': weatherDescription,
            'Pressure': f"{pressure} mb",
            'Sunrise': sunriseT,
            'Sunset': sunsetT
        }
        return jsonify(result) # Returns a dict in json format of all weather data
    else:
        return jsonify({'error': 'City not found'}), 404 # If API call is bad returns 404

if __name__ == '__main__':
    app.run(host=f"{IP}")