# coding: utf-8

"""
    Fugue API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.events_api import EventsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestEventsApi(unittest.TestCase):
    """EventsApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.events_api.EventsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_list_events(self):
        """Test case for list_events

        Lists drift, remediation, and compliance events for an environment.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()