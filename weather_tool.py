import requests

def get_weather(city):

    headers = {
        "User-Agent": "weather-agent-assignment (student project)",
        "Accept": "application/geo+json"
    }

    try:
        # Step 1: Get latitude & longitude from city
        geo_url = f"https://nominatim.openstreetmap.org/search?q={city}&format=json&limit=1"
        geo_response = requests.get(geo_url, headers=headers)

        geo_data = geo_response.json()

        if not geo_data:
            return "City not found."

        lat = geo_data[0]["lat"]
        lon = geo_data[0]["lon"]

        # Step 2: Get forecast endpoint
        points_url = f"https://api.weather.gov/points/{lat},{lon}"
        points_response = requests.get(points_url, headers=headers)

        if points_response.status_code != 200:
            return "Weather service unavailable."

        points_data = points_response.json()

        if "properties" not in points_data:
            return "Unexpected response from weather API."

        forecast_url = points_data["properties"]["forecast"]

        # Step 3: Get forecast
        forecast_response = requests.get(forecast_url, headers=headers)
        forecast_data = forecast_response.json()

        forecast = forecast_data["properties"]["periods"][0]

        return {
            "temperature": forecast["temperature"],
            "temperatureUnit": forecast["temperatureUnit"],
            "forecast": forecast["shortForecast"]
        }

    except Exception as e:
        return f"Error retrieving weather data: {str(e)}"