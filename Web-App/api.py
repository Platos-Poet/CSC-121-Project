from flask import Flask, jsonify
import requests

app = Flask(__name__)

OPENWEATHERMAP_API_KEY = "b2f82104ab9851dcf5b08eb56d3ede6a" # My personal API key

@app.route('/weather/<city>')
def get_weather(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHERMAP_API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        # Creating the reponse returned
        weatherData = response.json()
        temperature = round(weatherData['main']['temp'] - 273.15, 2) # convert temperature from Kelvin to Celsius
        humidity = weatherData['main']['humidity']
        windSpeed = weatherData['wind']['speed']
        weatherDescription = weatherData['weather'][0]['description']
        result = {
            'city': city,
            'temperature': temperature,
            'humidity': humidity,
            'windSpeed': windSpeed,
            'weatherDescription': weatherDescription
        }
        return jsonify(result) # Returns a dict in json format of all weather data
    else:
        return jsonify({'error': 'City not found'}), 404 # If API call is bad returns 404

if __name__ == '__main__':
    app.run()

