
import requests
import json
import sys

def get_weather_forecast(city_name):
    # Enter your OpenWeatherMap API key here
    api_key = "43cc35964dd1a12df551a91e3f544d4d"

    # API endpoint for current weather data
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

    try:
        # Send a GET request to the API endpoint
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if the request was unsuccessful
        weather_data = response.json()  # Parse the JSON response

        # Extract relevant information from the response
        weather_description = weather_data["weather"][0]["description"]
        temperature = weather_data["main"]["temp"]

        # Print the weather forecast
        print(f"Weather forecast for {city_name}:")
        print(f"Description: {weather_description}")
        print(f"Temperature: {temperature}°C")

    except requests.exceptions.RequestException as e:
        print(f"Error occurred while retrieving weather data: {str(e)}")
    except (KeyError, IndexError):
        print("Invalid response received from the weather API.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python weather_forecast.py <city_name>")
    else:
        city_name = sys.argv[1]
        get_weather_forecast(city_name)

