import requests


def get_coordinates(city):
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {
        "name": city,
        "count": 1
    }
    response = requests.get(url , params=params)
    response.raise_for_status()
    data = response.json()

    if "results" not in data:
        return None , None

    lat = data["results"][0]["latitude"]
    lon = data["results"][0]["longitude"]
    return lat, lon


def get_weather(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True
    }
    response = requests.get(url , params=params)
    response.raise_for_status()
    return response.json()

def display_weather(city , weather_data):
    current = weather_data["current_weather"]
    print("\n WEATHER REPORT")
    print("-" * 35)
    print(f"City: {city}")
    print(f"Temperature: {current['temperature']} °C")
    print(f"Wind Speed: {current['windspeed']} km/h")
    print(f"Weather Code: {current['weathercode']}")
    print("-" * 35)

def main():
    city = input("Enter city name: ").strip()

    try:
        lat, lon = get_coordinates(city)

        if lat is None:
            print(" City not found.")
            return

        weather_data = get_weather(lat, lon)
        display_weather(city, weather_data)

    except requests.exceptions.RequestException:
        print(" Network error. Please try again later.")


if __name__ == "__main__":
    main()


