import speech_recognition as sr
import pyttsx3
import requests
from datetime import datetime

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Your OpenWeatherMap API key
API_KEY = '082d30d854791f4ce0b44d3ba522b831'

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def get_weather(city):
    """Fetch weather data from OpenWeatherMap API with additional details."""
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temperature_c = data['main']['temp'] - 273.15  # Convert from Kelvin to Celsius
        temperature_f = (temperature_c * 9/5) + 32  # Convert Celsius to Fahrenheit
        
        feels_like_c = data['main']['feels_like'] - 273.15
        feels_like_f = (feels_like_c * 9/5) + 32

        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        description = data['weather'][0]['description']

        # Convert sunrise and sunset times from UNIX timestamps to readable format with local time
        sunrise = datetime.fromtimestamp(data['sys']['sunrise']).strftime('%Y-%m-%d %H:%M:%S')
        sunset = datetime.fromtimestamp(data['sys']['sunset']).strftime('%Y-%m-%d %H:%M:%S')
        
        return {
            "temperature_c": temperature_c,
            "temperature_f": temperature_f,
            "feels_like_c": feels_like_c,
            "feels_like_f": feels_like_f,
            "humidity": humidity,
            "wind_speed": wind_speed,
            "description": description,
            "sunrise": sunrise,
            "sunset": sunset
        }
    else:
        return None

def listen_for_city():
    """Listen for a city name from the user's voice."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please say the name of the city...")
        speak("Please say the name of the city...")
        audio = recognizer.listen(source)
        try:
            city = recognizer.recognize_google(audio)
            return city
        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand you. Please try again.")
        except sr.RequestError:
            speak("Sorry, there seems to be a problem with the speech recognition service.")
        return None

def listen_for_exit():
    """Listen for exit phrases."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for exit command...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio).lower()
            return command in ["thank you", "bye", "see you later","stop","exit"]
        except sr.UnknownValueError:
            return False
        except sr.RequestError:
            speak("Sorry, there seems to be a problem with the speech recognition service.")
            return False

def main():
    speak("Hello! I'm your weather assistant.")
    
    while True:
        city = listen_for_city()
        if city:
            weather_data = get_weather(city)
            if weather_data:
                weather_info = (
                    f"Temperature in {city}\t:\t {weather_data['temperature_c']:.2f}°C or {weather_data['temperature_f']:.2f}°F.\n"
                    f"Temperature feels like\t:\t {weather_data['feels_like_c']:.2f}°C or {weather_data['feels_like_f']:.2f}°F.\n"
                    f"Humidity\t:\t {weather_data['humidity']}%.\n"
                    f"Wind Speed\t:\t {weather_data['wind_speed']} m/s.\n"
                    f"General Weather\t:\t {weather_data['description']}.\n"
                    f"Sunrise in {city} at {weather_data['sunrise']} local time.\n"
                    f"Sunset in {city} at {weather_data['sunset']} local time."
                )
                print(weather_info)
                speak(weather_info)
            else:
                speak(f"Sorry, I couldn't retrieve the weather for {city}.")
        else:
            speak("Please try again and say a city name.")

        # Check for exit phrases
        speak("Would you like to check another city's weather?")
        if listen_for_exit():
            speak("Thank you for using the weather assistant. Goodbye!")
            break

if __name__ == "__main__":
    main()
