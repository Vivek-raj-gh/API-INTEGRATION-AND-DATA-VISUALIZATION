import requests
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

API_KEY = "9d7f3a2909f42fa21234cbc468f771c1"
CITY = "London"
BASE_URL = "http://api.openweathermap.org/data/2.5/forecast"

def fetch_weather_data(city: str, api_key: str):
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    return response.json()

def process_weather_data(data):
    dates = []
    temperatures = []

    for entry in data["list"]:
        date = datetime.fromtimestamp(entry["dt"])
        temp = entry["main"]["temp"]
        dates.append(date)
        temperatures.append(temp)

    return dates, temperatures

def plot_weather(dates, temperatures):
    plt.figure(figsize=(12, 6))
    sns.lineplot(x=dates, y=temperatures, marker="o")
    plt.title(f"Temperature Forecast for {CITY}")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    try:
        weather_data = fetch_weather_data(CITY, API_KEY)
        dates, temps = process_weather_data(weather_data)
        plot_weather(dates, temps)
    except requests.RequestException as e:
        print("Error fetching weather data:", e)
