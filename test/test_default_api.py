# coding: utf-8

"""
    TeamCity REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 10.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import dohq_teamcity
from dohq_teamcity.api.default_api import DefaultApi  # noqa: E501
from dohq_teamcity.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = dohq_teamcity.api.default_api.DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_serve_api_version(self):
        """Test case for serve_api_version

        """
        pass

    def test_serve_build_field_short(self):
        """Test case for serve_build_field_short

        """
        pass

    def test_serve_plugin_info(self):
        """Test case for serve_plugin_info

        """
        pass

    def test_serve_root(self):
        """Test case for serve_root

        """
        pass

    def test_serve_version(self):
        """Test case for serve_version

        """
        pass


if __name__ == '__main__':
    unittest.main()
