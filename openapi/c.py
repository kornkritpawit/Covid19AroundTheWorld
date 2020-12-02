import sys
from flask import abort
import pymysql as mysql
from config import OPENAPI_AUTOGEN_DIR, DB_HOST, DB_USER, DB_PASSWD, DB_NAME

sys.path.append(OPENAPI_AUTOGEN_DIR)
from openapi_server import models

def db_cursor():
    return mysql.connect(host=DB_HOST,user=DB_USER,passwd=DB_PASSWD,db=DB_NAME).cursor()

def get_countries():
    with db_cursor() as cs:
        cs.execute("SELECT CountryID, CountryName, CountryAlpha2, CountryAlpha3 FROM Country")
        result = [models.Country(*row) for row in cs.fetchall()]
        return result

def get_country_details(countryId):
    with db_cursor() as cs:
        cs.execute("""
            SELECT CountryID, CountryName, CountryAlpha2, CountryAlpha3
            FROM Country
            WHERE CountryID=%s
            """, [countryId])
        result = cs.fetchone()
    if result:
        CountryID, CountryName, CountryAlpha2, CountryAlpha3 = result
        return models.Country(*result)
    else:
        abort(404)

def get_sum_covid19_situation_world():
    with db_cursor() as cs:

        return result

def get_new_covid19_situation_world():
    with db_cursor() as cs:
        return result

def get_sum_covid19_situation_in_all_country():
    with db_cursor() as cs:
        return result

def get_new_covid19_situation_in_all_country():
    with db_cursor() as cs:
        return result

def get_covid19_situation_total_cases():
    with db_cursor() as cs:
        return result

def get_covid19_situation_death_cases():
    with db_cursor() as cs:
        return result

def get_covid19_situation_recovered_cases():
    with db_cursor() as cs:
        return result

def get_covid19_situation_new_cases():
    with db_cursor() as cs:
        return result

def get_covid19_situation_new_death():
    with db_cursor() as cs:
        return result

def get_covid19_situation_new_recovered():
    with db_cursor() as cs:
        return result

def get_covid19_information_in_specific_country():
    with db_cursor() as cs:
        return result

def get_currency_rates():
    with db_cursor() as cs:
        return result

def get_currency_rate_in_specific_country():
    with db_cursor() as cs:
        return result

def get_currency_unit_in_specific_country():
    with db_cursor() as cs:
        return result
        

# def get_world_currency_symbols():
#     response = requests.get("http://data.fixer.io/api/symbols?access_key=" + access_key)
#     symbols = response.json()["symbols"]
#     return models.Symbols(symbols)


# def get_world_currency_rates():
#     response = requests.get("http://data.fixer.io/api/latest?access_key=" + access_key)
#     date = response.json()["date"]
#     rates = response.json()["rates"]
#     base = response.json()["base"]
#     return models.Currency(rates, base, date)


# def get_world_currency_rates_with_symbols(sym):
#     response = requests.get("http://data.fixer.io/api/latest?access_key=" + access_key + "&symbols=" + sym)
#     date = response.json()["date"]
#     rates = response.json()["rates"]
#     base = response.json()["base"]
#     return models.Currency(rates, base, date)


# def get_covid_by_date_and_country(date, country):
#     """ Date format example 2020-11-24"""
#     response = requests.get("https://api.covid19tracking.narrativa.com/api/" + date + "/country/" + country)
#     data = response.json()["dates"][date]["countries"][country.capitalize()]
#     country_query = data["name"]
#     confirmed = data["today_confirmed"]
#     deaths = data["today_deaths"]
#     return models.CovidCase(country_query, confirmed, deaths)


# def get_weather_currently_from_one_location(city_name, unit='metric'):
#     """City name can be country. Unit choose between 'metric' and 'imperial'"""
#     response = requests.get(
#         "http://api.openweathermap.org/data/2.5/weather?q=" + city_name + "&appid=9a02e2dc4526ef064473d026b12125e2"
#                                                                           "&units=" + unit)
#     name = response.json()["name"]
#     country = response.json()["sys"]["country"]
#     data = response.json()["main"]
#     temp = data["temp"]
#     feels_like = data["feels_like"]
#     temp_min = data["temp_min"]
#     temp_max = data["temp_max"]
#     pressure = data["pressure"]
#     humidity = data["humidity"]
#     return models.Weather(name, country, temp, feels_like, temp_min, temp_max, pressure, humidity)
