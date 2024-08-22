#Intro to Api

'''import pyowm

owm = pyowm.OWM('5a2ce758b335a7d5a6a95520133f03a4')
mgr= owm.weather_manager()
observation = mgr.weather_at_place('London,uk')
w = observation.weather

print(f'The Humidity in London is {w.humidity} \nThe wind in London is {w.wind()}')

observation_hk = mgr.weather_at_place('Hong Kong,China')
w_hk= observation.weather
print(f'The Humidity in Hong Kong is {w_hk.humidity}')

observation_hk = mgr.weather_at_place('Tokyo,Japan')
w_hk= observation.weather
print(f'The Temperature in Tokyo is {w_hk.temperature()}')

observation_hk = mgr.weather_at_place('Tokyo,Japan')
w_hk= observation.weather
print(f'The Windspeed in Tokyo is {w_hk.wind()}')'''

#REST APIS
'''from pprint import pprint
import requests
r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=London&APPID=5a2ce758b335a7d5a6a95520133f03a4')
pprint(r.json())'''

