import sqlite3
import requests
import matplotlib.pyplot as plt
from datetime import datetime

# Constants
DB_NAME = 'data/weather_data.db'
API_KEY = 'your_openweathermap_api_key'  # Replace with your actual API key
CITIES = ['Delhi', 'Mumbai', 'Bangalore', 'Kolkata', 'Chennai']
THRESHOLD = 30  # Temperature threshold for alerts

def fetch_weather_data(city):
    """Fetch weather data from OpenWeatherMap API."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data for {city}: {response.status_code}")
        return None

def insert_weather_data(city, avg_temp, max_temp, min_temp, condition, date):
    """Insert weather data into the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO daily_summaries (city, avg_temperature, max_temperature, min_temperature, dominant_condition, date)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (city, avg_temp, max_temp, min_temp, condition, date))
    conn.commit()
    conn.close()

def plot_daily_summaries():
    """Plot daily summaries of weather data for specified cities."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute('SELECT city, AVG(avg_temperature) AS avg_temp FROM daily_summaries GROUP BY city')
    data = cursor.fetchall()
    conn.close()

    if not data:
        print("No data found to plot.")
        return

    cities = [row[0] for row in data]
    avg_temps = [row[1] for row in data]

    plt.bar(cities, avg_temps, color='blue')
    plt.xlabel('Cities')
    plt.ylabel('Average Temperature (°C)')
    plt.title('Average Daily Temperatures')
    plt.xticks(rotation=45)
    plt.tight_layout()  # Adjust layout to prevent clipping of labels
    plt.show()

def plot_historical_trends(city):
    """Plot historical temperature trends for a specific city."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute('SELECT date, avg_temperature FROM daily_summaries WHERE city = ? ORDER BY date', (city,))
    data = cursor.fetchall()
    conn.close()

    if not data:
        print(f"No historical data found for {city}.")
        return

    dates = [row[0] for row in data]
    avg_temps = [row[1] for row in data]

    plt.plot(dates, avg_temps, marker='o')
    plt.xlabel('Date')
    plt.ylabel('Average Temperature (°C)')
    plt.title(f'Historical Temperature Trends for {city}')
    plt.xticks(rotation=45)
    plt.tight_layout()  # Adjust layout to prevent clipping of labels
    plt.show()

def trigger_alerts(city, threshold):
    """Check the average temperature and trigger alerts if necessary."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute('SELECT AVG(avg_temperature) FROM daily_summaries WHERE city = ?', (city,))
    avg_temp = cursor.fetchone()[0]
    conn.close()

    if avg_temp is not None:
        if avg_temp > threshold:
            print(f"Alert! The average temperature in {city} has exceeded {threshold}°C. Current average: {avg_temp:.2f}°C.")
        else:
            print(f"No alerts. The average temperature in {city} is within the safe range ({avg_temp:.2f}°C).")
    else:
        print(f"No temperature data available for {city}.")

if __name__ == "__main__":
    # Fetch and insert data for each city
    for city in CITIES:
        weather_data = fetch_weather_data(city)
        if weather_data:
            main_temp = weather_data['main']
            avg_temp = main_temp['temp']
            max_temp = main_temp['temp_max']
            min_temp = main_temp['temp_min']
            condition = weather_data['weather'][0]['description']
            date = datetime.now().strftime('%Y-%m-%d')
            insert_weather_data(city, avg_temp, max_temp, min_temp, condition, date)

    print("Displaying daily summaries...")
    plot_daily_summaries()  # Plot daily summaries for all cities

    # Plot historical trends and trigger alerts for each city
    for city in CITIES:
        print(f"\nDisplaying historical trends for {city}...")
        plot_historical_trends(city)  # Plot historical trends for each city
        trigger_alerts(city, THRESHOLD)  # Trigger alerts based on temperature threshold
