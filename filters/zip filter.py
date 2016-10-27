import requests
from pprint import pprint

postal_address = raw_input("Enter the your postal address or zip code: ")
APPID = raw_input("Enter APP_ID/api-key from the website: ")

def weather(city):
	r = requests.get("http://api.openweathermap.org/data/2.5/forecast/weather?q={}&APPID={}".format(city,APPID))
	return r

def get_city(zip_code):
	city_info = requests.get("http://maps.googleapis.com/maps/api/geocode/json?address={}&sensor=false".format(zip_code))
	city_name = city_info.json()['results'][0]['address_components'][1]['long_name']
	return city_name


city = get_city(postal_address)
info = weather(city)
pprint(info.json())
