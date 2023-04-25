from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

OPENWEATHERMAP_API_KEY = "b2f82104ab9851dcf5b08eb56d3ede6a"

@app.route('/weather/<city>')
def get_weather(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q=Ruston&appid=b2f82104ab9851dcf5b08eb56d3ede6a'
    response = requests.get(url)
    if response.status_code == 200:
        weatherData = response.json()
        temperature = round(weatherData['main']['temp'] - 273.15, 2) # convert temperature from Kelvin to Celsius
        humidity = weatherData['main']['humidity']
        wind_speed = weatherData['wind']['speed']
        weather_description = weatherData['weather'][0]['description']
        result = {
            'city': city,
            'temperature': temperature,
            'humidity': humidity,
            'wind_speed': wind_speed,
            'weather_description': weather_description
        }
        return jsonify(result)
    else:
        return jsonify({'error': 'City not found'}), 404

if __name__ == '__main__':
    app.run()

