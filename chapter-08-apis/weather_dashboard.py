# Weather Dashboard - Chapter 8 Project

import requests


def get_weather(city):
    """Fetch weather data from wttr.in API"""
    url = f"https://wttr.in/{city}?format=j1"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error: Could not fetch weather (status {response.status_code})")
        return None

    return response.json()


def display_weather(data):
    """Display current weather conditions"""
    current = data["current_condition"][0]
    area = data["nearest_area"][0]["areaName"][0]["value"]

    print(f"\n{'=' * 40}")
    print(f"  Weather in {area}")
    print(f"{'=' * 40}")
    print(f"  Temperature:  {current['temp_C']}°C")
    print(f"  Feels like:   {current['FeelsLikeC']}°C")
    print(f"  Condition:    {current['weatherDesc'][0]['value']}")
    print(f"  Humidity:     {current['humidity']}%")
    print(f"  Wind:         {current['windspeedKmph']} km/h")
    print(f"{'=' * 40}")


def display_forecast(data):
    """Display 3-day forecast"""
    print(f"\n  3-Day Forecast:")
    print(f"  {'-' * 35}")
    for day in data["weather"][:3]:
        date = day["date"]
        high = day["maxtempC"]
        low = day["mintempC"]
        desc = day["hourly"][4]["weatherDesc"][0]["value"]
        print(f"  {date}:  {low}°C - {high}°C  ({desc})")


# Main program
print("=" * 40)
print("  WEATHER DASHBOARD")
print("=" * 40)

while True:
    print("\n1. Check Weather")
    print("2. Compare Two Cities")
    print("3. Exit")

    choice = input("\nChoice: ")

    if choice == "1":
        city = input("Enter city: ").strip()
        data = get_weather(city)
        if data:
            display_weather(data)
            display_forecast(data)

    elif choice == "2":
        city1 = input("First city: ").strip()
        city2 = input("Second city: ").strip()
        data1 = get_weather(city1)
        data2 = get_weather(city2)
        if data1:
            display_weather(data1)
        if data2:
            display_weather(data2)

    elif choice == "3":
        print("Goodbye!")
        break
