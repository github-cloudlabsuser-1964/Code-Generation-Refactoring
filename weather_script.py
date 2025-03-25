import requests

def get_weather(city):
    api_key = "your_api_key_here"  # Replace with your AccuWeather API key
    location_url = f"http://dataservice.accuweather.com/locations/v1/cities/search"
    weather_url = f"http://dataservice.accuweather.com/currentconditions/v1/"

    # Step 1: Get the location key for the city
    location_params = {
        "apikey": api_key,
        "q": city
    }
    location_response = requests.get(location_url, params=location_params)
    if location_response.status_code == 200:
        location_data = location_response.json()
        if not location_data:
            return "City not found."
        location_key = location_data[0]["Key"]
    else:
        return "Error fetching location data."

    # Step 2: Get the current weather using the location key
    weather_params = {
        "apikey": api_key
    }
    weather_response = requests.get(weather_url + location_key, params=weather_params)
    if weather_response.status_code == 200:
        weather_data = weather_response.json()
        if weather_data:
            weather = weather_data[0]["WeatherText"]
            temperature = weather_data[0]["Temperature"]["Metric"]["Value"]
            return f"Weather in {city}: {weather}, Temperature: {temperature}°C"
        else:
            return "Weather data not available."
    else:
        return "Error fetching weather data."

def main():
    print("Welcome to the Weather Consulting App!")
    while True:
        city = input("Enter a city name (or type 'exit' to quit): ")
        if city.lower() == "exit":
            print("Goodbye!")
            break
        print(get_weather(city))

if __name__ == "__main__":
    main()