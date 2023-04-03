import pyowm

# Initialize Weather Data in a Location
owm = pyowm.OWM('ba799f05aec562a296770c57b576d16a')
mgr = owm.weather_manager()
observation = mgr.weather_at_place('Ruston, Louisiana')
w = observation.weather

# Basic Weather Readout
temp = w.temperature('fahrenheit')
status = w.detailed_status
print("It is currently " + str(int(temp['temp'])) + " degrees and " + status)

# Temperature Forcast Dict
temp_dict_fahrenheit = w.temperature('fahrenheit')  # a dict in Fahrenheit units
temp_dict_celsius = w.temperature('celsius')  # guess?
print(f"{temp_dict_fahrenheit}")

# Wind Speed Testing
wind_dict_in_mph = w.wind(unit='miles_hour')   # Default unit: 'meters_sec'
windSpeed =wind_dict_in_mph['speed'] # Average Speed
windDeg = wind_dict_in_mph['deg'] # Degree (Direction) of wind
print(f"{wind_dict_in_mph}")

# Barometric Pressure Measurements
pressure_dict = w.barometric_pressure(unit='inHg') # Gets pressure in inHg, US standard measurement
print(f"{pressure_dict}")

# Sunrise/Sunset info
sunrise_date = w.sunrise_time(timeformat='date')
sunset_date = w.sunset_time(timeformat='date')
print(f"Sunrise :{sunrise_date}\nSunset: {sunset_date}") # Prints Sunrise/Sunset as python datetime.datetime object

