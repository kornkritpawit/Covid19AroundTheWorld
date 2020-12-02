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

def get_new_covid19_situation_world():
    with db_cursor() as cs:
        cs.execute("""
            SELECT Location, NewCase, NewDeath, Date
            FROM Covid19 
            WHERE Location = "World"
            """)
        result = [models.Covid19WorldNew(*row) for row in cs.fetchall()]
        return result

def get_sum_covid19_situation_in_all_country_latest():
    with db_cursor() as cs:
        cs.execute("""
        SELECT CountryID,CountryName,MAX(TotalCase) as TotalCase , MAX(TotalDeath) as TotalDeath, MAX(TotalRecovered) as TotalRecovered,MAX(Date) as Date FROM
        (SELECT CountryID as CountryID, CountryName, TotalCase, TotalDeath, Covid19Recovered.TotalRecovered as TotalRecovered , Covid19.Date as Date
        FROM Country INNER JOIN Covid19 INNER JOIN Covid19Recovered 
        WHERE Covid19.CountryAlpha3 = Country.CountryAlpha3
        AND Country.CountryAlpha2 = Covid19Recovered.CountryAlpha2) c
        GROUP BY CountryID,CountryName
        """)
        result = [models.Covid19CountrySum(*row) for row in cs.fetchall()]
        return result

def get_new_covid19_situation_in_all_country():
    with db_cursor() as cs:
        cs.execute("""
        SELECT CountryID, CountryName, NewCase, NewDeath, Covid19.Date
        FROM Country INNER JOIN Covid19 
        WHERE Covid19.CountryAlpha3 = Country.CountryAlpha3
        """)
        result = [models.Covid19CountryNew(*row) for row in cs.fetchall()]
        return result

def get_new_covid19_situation_in_specific_country(countryId):
    with db_cursor() as cs:
        cs.execute("""
        SELECT CountryID, CountryName, NewCase, NewDeath, Covid19.Date
        FROM Country INNER JOIN Covid19 
        WHERE Covid19.CountryAlpha3 = Country.CountryAlpha3
        AND CountryID=%s
        """, countryId)
        result = [models.Covid19CountryNew(*row) for row in cs.fetchall()]
        return result

def get_currency_rate_in_specific_country(countryId):
    with db_cursor() as cs:
        cs.execute("""
        SELECT CountryID, CountryName, CurrencyRate.Rate, CurrencySymbol.Symbol, CurrencyRate.Date 
        FROM Country INNER JOIN CurrencySymbol INNER JOIN CurrencyRate 
        WHERE CurrencySymbol.Symbol = CurrencyRate.SymbolAlpha
        AND Country.CountryAlpha2 = CurrencySymbol.CountryAlpha2 AND CountryID=%s
        """, countryId)
        result = [models.Currency(*row) for row in cs.fetchall()]
        return result

def get_currency_unit_in_specific_country(countryId):
    with db_cursor() as cs:
        cs.execute("""
        SELECT CountryName, Symbol FROM
        (SELECT CountryID, CountryName, CurrencyRate.Rate, CurrencySymbol.Symbol as Symbol, CurrencyRate.Date 
        FROM Country INNER JOIN CurrencySymbol INNER JOIN CurrencyRate 
        WHERE CurrencySymbol.Symbol = CurrencyRate.SymbolAlpha
        AND Country.CountryAlpha2 = CurrencySymbol.CountryAlpha2 AND CountryID=%s) c
        GROUP BY CountryName, Symbol
        """, countryId)
        result = [models.CurrencyUnit(*row) for row in cs.fetchall()]
        return result
