import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests
import time
from datetime import datetime
import matplotlib.pyplot as plt

# OpenWeatherMap API setup
API_KEY = '082d30d854791f4ce0b44d3ba522b831'
CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
ALERT_THRESHOLD_TEMP = 35  # Example threshold in Celsius

# Email alert setup
SMTP_SERVER = 'smtp.gmail.com'  # for Gmail
SMTP_PORT = 587
EMAIL_ADDRESS = 'likhithakanuru@gmail.com'
EMAIL_PASSWORD = 'ekdb tovw qkya qqry'
TO_EMAIL = '213j1a4252@raghuinstech.com'

# Function to send email alerts
def send_email_alert(city, temp):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = TO_EMAIL
    msg['Subject'] = f"Weather Alert: High Temperature in {city}"
    
    body = f"The temperature in {city} has reached {temp:.2f}°C, exceeding the threshold of {ALERT_THRESHOLD_TEMP}°C."
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
            print(f"Email alert sent for {city} with temperature {temp:.2f}°C")
    except Exception as e:
        print(f"Failed to send email alert: {e}")

# Function to convert Kelvin to Celsius
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

# Function to fetch weather data
def fetch_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather_data = {
            'city': city,
            'temp': kelvin_to_celsius(data['main']['temp']),
            'feels_like': kelvin_to_celsius(data['main']['feels_like']),
            'condition': data['weather'][0]['main'],
            'timestamp': datetime.now()
        }
        return weather_data
    else:
        print(f"Error fetching data for {city}")
        return None

# Function to monitor weather and trigger alerts
def monitor_weather():
    daily_data = []
    for city in CITIES:
        data = fetch_weather(city)
        if data:
            daily_data.append(data)
            print(f"Weather in {city}: {data['temp']}°C, Condition: {data['condition']}")
            
            # Alert system
            if data['temp'] > ALERT_THRESHOLD_TEMP:
                print(f"Alert! Temperature in {city} exceeds threshold with {data['temp']}°C")
                send_email_alert(city, data['temp'])
    
    return daily_data

# Visualization
def plot_weather_data(daily_data):
    cities = [data['city'] for data in daily_data]
    temps = [data['temp'] for data in daily_data]
    plt.bar(cities, temps, color='skyblue')
    plt.xlabel('City')
    plt.ylabel('Temperature (°C)')
    plt.title('Temperature in Major Indian Cities')
    plt.show()

# Main function to periodically fetch and monitor weather data
def main():
    interval = 300  # Fetch data every 5 minutes
    try:
        while True:
            print("\nFetching weather data...")
            daily_data = monitor_weather()
            plot_weather_data(daily_data)
            time.sleep(interval)
    except KeyboardInterrupt:
        print("Monitoring stopped.")

if __name__ == "__main__":
    main()
