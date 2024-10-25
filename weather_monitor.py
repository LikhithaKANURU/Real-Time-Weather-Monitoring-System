import requests
import time
from config import API_KEY, CITIES, INTERVAL, TEMP_THRESHOLD
import schedule
from datetime import datetime

# Dictionary to store weather data for each city
weather_data = {}

# Convert temperature from Kelvin to Celsius
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

# Fetch weather data from OpenWeatherMap API for a given city
def fetch_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    response = requests.get(url)
    data = response.json()

    # Debugging: Print the entire API response
    print(f"API response for {city}: {data}")

    # Check for an error code in the API response
    if data.get("cod") != 200:
        print(f"Error fetching weather data for {city}: {data.get('message', 'Unknown error')}")
        return None  # Skip processing for this city if an error occurs

    # Extract weather data
    temp = kelvin_to_celsius(data['main']['temp'])
    feels_like = kelvin_to_celsius(data['main']['feels_like'])
    main_condition = data['weather'][0]['main']
    timestamp = data['dt']

    return {
        'city': city,
        'temp': temp,
        'feels_like': feels_like,
        'condition': main_condition,
        'timestamp': timestamp,
    }

# Update weather data for all cities and check for alerts
def update_weather_data():
    global weather_data
    for city in CITIES:
        weather = fetch_weather(city)
        if weather is None:
            continue  # Skip this city if there was an error
        print(f"Weather in {city}: {weather['temp']}C, {weather['condition']} at {datetime.utcfromtimestamp(weather['timestamp'])}")
        if city not in weather_data:
            weather_data[city] = []
        weather_data[city].append(weather)

    check_alerts()

# Check for alerts based on temperature thresholds
def check_alerts():
    for city, data in weather_data.items():
        if len(data) < 2:
            continue  # Need at least two data points to check consecutive temperature breaches
        last_temp = data[-1]['temp']
        prev_temp = data[-2]['temp']
        if last_temp > TEMP_THRESHOLD and prev_temp > TEMP_THRESHOLD:
            print(f"ALERT: Temperature exceeded {TEMP_THRESHOLD}C in {city}!")

# Calculate daily weather summary for each city
def calculate_daily_summary():
    for city, data in weather_data.items():
        if not data:
            continue
        today = datetime.utcfromtimestamp(data[-1]['timestamp']).date()

        # Filter data for the current day
        daily_data = [d for d in data if datetime.utcfromtimestamp(d['timestamp']).date() == today]

        if not daily_data:
            continue

        # Calculate average, max, and min temperatures
        avg_temp = sum([d['temp'] for d in daily_data]) / len(daily_data)
        max_temp = max([d['temp'] for d in daily_data])
        min_temp = min([d['temp'] for d in daily_data])
        dominant_condition = max(set([d['condition'] for d in daily_data]), key=[d['condition'] for d in daily_data].count)

        # Print daily summary
        print(f"Daily Summary for {city} on {today}:")
        print(f"Average Temp: {avg_temp:.2f}C, Max Temp: {max_temp:.2f}C, Min Temp: {min_temp:.2f}C, Dominant Condition: {dominant_condition}")

# Schedule tasks to fetch weather data and calculate daily summaries
schedule.every(INTERVAL).minutes.do(update_weather_data)  # Fetch data at regular intervals
schedule.every().day.at("23:59").do(calculate_daily_summary)  # Calculate daily summary at the end of the day

if __name__ == "__main__":
    update_weather_data()  # Fetch data once immediately
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)  # Sleep to avoid busy waiting
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
