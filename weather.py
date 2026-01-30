import requests

API_KEY = "2b76fdc8dc3bd4e4a78ae2cf198131bd"  # replace with your OpenWeatherMap API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name: ")

params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"  # Celsius
}

response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    data = response.json()

    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather_condition = data["weather"][0]["description"]

    print("\n🌤 Weather Information")
    print(f"City: {city}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {weather_condition.capitalize()}")

else:
    print("❌ City not found or API error.")
    
"""
Output:-
Enter city name: Pune

🌤 Weather Information
City: Pune
Temperature: 24.67°C
Humidity: 51%
Condition: Scattered clouds
"""