import sys

import requests
from config import OPENAPI_AUTOGEN_DIR

sys.path.append(OPENAPI_AUTOGEN_DIR)
from openapi_server import models

access_key = "35c77d0f34c27b8a918447ade3037e6d"


def get_world_currency_symbols():
    response = requests.get("http://data.fixer.io/api/symbols?access_key=" + access_key)
    symbols = response.json()["symbols"]
    return models.Symbols(symbols)


def get_world_currency_rates():
    response = requests.get("http://data.fixer.io/api/latest?access_key=" + access_key)
    date = response.json()["date"]
    rates = response.json()["rates"]
    base = response.json()["base"]
    return models.Currency(rates, base, date)


def get_world_currency_rates_with_symbols(sym):
    response = requests.get("http://data.fixer.io/api/latest?access_key=" + access_key + "&symbols=" + sym)
    date = response.json()["date"]
    rates = response.json()["rates"]
    base = response.json()["base"]
    return models.Currency(rates, base, date)


def get_covid_by_date_and_country(date, country):
    """ Date format example 2020-11-24"""
    response = requests.get("https://api.covid19tracking.narrativa.com/api/" + date + "/country/" + country)
    data = response.json()["dates"][date]["countries"][country.capitalize()]
    country_query = data["name"]
    confirmed = data["today_confirmed"]
    deaths = data["today_deaths"]
    return models.CovidCase(country_query, confirmed, deaths)


def get_weather_currently_from_one_location(city_name, unit='metric'):
    """City name can be country. Unit choose between 'metric' and 'imperial'"""
    response = requests.get(
        "http://api.openweathermap.org/data/2.5/weather?q=" + city_name + "&appid=9a02e2dc4526ef064473d026b12125e2"
                                                                          "&units=" + unit)
    name = response.json()["name"]
    country = response.json()["sys"]["country"]
    data = response.json()["main"]
    temp = data["temp"]
    feels_like = data["feels_like"]
    temp_min = data["temp_min"]
    temp_max = data["temp_max"]
    pressure = data["pressure"]
    humidity = data["humidity"]
    return models.Weather(name, country, temp, feels_like, temp_min, temp_max, pressure, humidity)
