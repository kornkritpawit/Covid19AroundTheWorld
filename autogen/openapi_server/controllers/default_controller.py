import connexion
import six

from openapi_server.models.currency import Currency  # noqa: E501
from openapi_server.models.symbols import Symbols  # noqa: E501
from openapi_server import util


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
