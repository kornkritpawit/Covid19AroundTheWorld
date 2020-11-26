import connexion
import six

from openapi_server.models.covid_case import CovidCase  # noqa: E501
from openapi_server.models.currency import Currency  # noqa: E501
from openapi_server.models.symbols import Symbols  # noqa: E501
from openapi_server import util


def controller_get_covid_by_date_and_country(country, date):  # noqa: E501
    """Returns complete details of the specified covid all time

     # noqa: E501

    :param country: 
    :type country: str
    :param date: 
    :type date: str

    :rtype: CovidCase
    """
    return 'do some magic!'


def controller_get_world_currency_rates():  # noqa: E501
    """Returns a list of currencies.

     # noqa: E501


    :rtype: List[Currency]
    """
    return 'do some magic!'


def controller_get_world_currency_rates_with_symbols(sym):  # noqa: E501
    """Returns complete details of the specified symbols of currency

     # noqa: E501

    :param sym: 
    :type sym: str

    :rtype: Currency
    """
    return 'do some magic!'


def controller_get_world_currency_symbols():  # noqa: E501
    """Returns a list of symbols.

     # noqa: E501


    :rtype: List[Symbols]
    """
    return 'do some magic!'
