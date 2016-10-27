""" weather Updates
    Usage:
        weather -h,--help
        weather <location> [ -j ]
        weather <repeating> ...
    Options:
        -h,--help       : show this help message
        location        : location can be an ip address ,zip-code or city name
        repeating       : example of repeating arguments
        -j,--json       : show the json file of the lookup
"""

from .utils import valid_city, valid_post, valid_ip
from docopt import docopt
import requests
from pprint import pprint
from utils import APP_ID
from datetime import datetime
import time

def weather(city):
    r = requests.get(
        "http://api.openweathermap.org/data/2.5/forecast/weather?q={}&APPID={}".format(city, APP_ID))
    return r.json()


def get_city_zip(zip_code):
    city_info = requests.get(
        "http://maps.googleapis.com/maps/api/geocode/json?address={}&sensor=false&app_id={}".format(zip_code, APP_ID))
    city_name = city_info.json()['results'][0][
        'address_components'][1]['long_name']
    return weather(city_name)


def get_city_ip(ip):
    url = 'http://ipinfo.io/' + ip + '/json'
    return requests.get(url).json()['city']
