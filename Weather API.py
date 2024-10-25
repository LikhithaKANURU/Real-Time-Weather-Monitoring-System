import datetime as dt 
import requests

BASE_URL="http://api.openweathermap.org/data/2.5/weather?"
API_KEY="082d30d854791f4ce0b44d3ba522b831"
#API_KEY=open('api_key','r').read()
CITY=input("Enter Your City : ")

def kel_to_cel_fah(kelvin):
    celsius=kelvin-273.15
    fahrenheit=celsius*(9/5)+32
    return celsius, fahrenheit

url =BASE_URL+"appid="+API_KEY+"&q="+CITY
response=requests.get(url).json()

temp_kel=response['main']['temp']
temp_celcius,temp_fah=kel_to_cel_fah(temp_kel)
feels_like_kelvin=response['main']['feels_like']
feels_like_cel,feels_like_far=kel_to_cel_fah(feels_like_kelvin)
wind_speed=response['wind']['speed']
humidity=response['main']['humidity']
description=response['weather'][0]['description']
sunrise_time=dt.datetime.utcfromtimestamp(response['sys']['sunrise']+response['timezone'])
sunset_time=dt.datetime.utcfromtimestamp(response['sys']['sunset']+response['timezone'])

print(response)
print(f"Temperature in  {CITY} : {temp_celcius:.2f}'C or {temp_fah:.2f}'F")
print(f"Temperature in  {CITY} feels like : {feels_like_cel:.2f}'C or {feels_like_far:.2f}'F")
print(f"Humidity in  {CITY} : {humidity}%")
print(f"Wind Speed in  {CITY} : {wind_speed}m/s")
print(f"General Weather in {CITY} : {description}")
print(f"Sun rise in {CITY} at {sunrise_time} local time.")
print(f"Sun set in {CITY} at {sunset_time} local time.")
