# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.currency import Currency  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_controller_get_currency(self):
        """Test case for controller_get_currency

        Returns complete details of the specified base and symbols of currency
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/covid-api/v1/currency/{base}/{sym}'.format(base='base_example', sym='sym_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
