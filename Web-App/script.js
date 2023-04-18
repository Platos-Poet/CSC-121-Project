// Function to make API request and display weather data
function getWeather(city) {
  $.get(`http://127.0.0.1:5000/weather/${city}`, function(data) {
      $('#weather-data').html(`
          <p><strong>City:</strong> ${data.city}</p>
          <p><strong>Temperature:</strong> ${data.temperature} &deg;C</p>
          <p><strong>Humidity:</strong> ${data.humidity} %</p>
          <p><strong>Wind Speed:</strong> ${data.wind_speed} m/s</p>
          <p><strong>Weather Description:</strong> ${data.weather_description}</p>
      `);
      $('#weather-data').show();
  }).fail(function() {
      $('#weather-data').html(`<p>Error: City not found</p>`);
      $('#weather-data').show();
  });
}

// Function to handle form submission
$('form').submit(function(event) {
  event.preventDefault();
  let city = $('#city').val();
  getWeather(city);
});