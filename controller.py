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

def get_sum_covid19_situation_world_latest():
    with db_cursor() as cs:
        cs.execute("""
            SELECT re.TotalCase, re.TotalDeath, re.TotalRecovered, re.Date
            FROM (SELECT MAX(cr.TotalRecovered) TotalRecovered, MAX(co.TotalCase) 
            TotalCase, MAX(co.TotalDeath) TotalDeath, MAX(co.Date) Date 
            FROM Covid19Recovered cr INNER JOIN Covid19 co ON cr.Location = co.Location) re
            """)
        result = [models.Covid19WorldSum(*row) for row in cs.fetchall()]
        return result

def get_new_covid19_situation_world_latest():
    with db_cursor() as cs:
        cs.execute("""
            SELECT re.TotalCase, re.TotalDeath, re.TotalRecovered, re.Date
            FROM (SELECT MAX(cr.TotalRecovered) TotalRecovered, MAX(co.TotalCase) 
            TotalCase, MAX(co.TotalDeath) TotalDeath, MAX(co.Date) Date 
            FROM Covid19Recovered cr INNER JOIN Covid19 co ON cr.Location = co.Location) re
            """)
        result = [models.Covid19WorldSum(*row) for row in cs.fetchall()]
        return result

def get_sum_covid19_situation_in_all_country_latest():
    with db_cursor() as cs:
        return "Hoy"

def get_new_covid19_situation_in_all_country():
    with db_cursor() as cs:
        return result
def get_covid19_information_in_specific_country():
    with db_cursor() as cs:
        return "Hoy"

def get_currency_rates():
    with db_cursor() as cs:
        return "Hoy"

def get_currency_rate_in_specific_country():
    with db_cursor() as cs:
        return "Hoy"

def get_currency_unit_in_specific_country():
    with db_cursor() as cs:
        return "Hoy"
        

