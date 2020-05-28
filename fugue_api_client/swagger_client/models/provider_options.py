# coding: utf-8

"""
    Fugue API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.provider_options_aws import ProviderOptionsAws  # noqa: F401,E501
from swagger_client.models.provider_options_azure import ProviderOptionsAzure  # noqa: F401,E501


class ProviderOptions(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'aws': 'ProviderOptionsAws',
        'aws_govcloud': 'ProviderOptionsAws',
        'azure': 'ProviderOptionsAzure'
    }

    attribute_map = {
        'aws': 'aws',
        'aws_govcloud': 'aws_govcloud',
        'azure': 'azure'
    }

    def __init__(self, aws=None, aws_govcloud=None, azure=None):  # noqa: E501
        """ProviderOptions - a model defined in Swagger"""  # noqa: E501

        self._aws = None
        self._aws_govcloud = None
        self._azure = None
        self.discriminator = None

        if aws is not None:
            self.aws = aws
        if aws_govcloud is not None:
            self.aws_govcloud = aws_govcloud
        if azure is not None:
            self.azure = azure

    @property
    def aws(self):
        """Gets the aws of this ProviderOptions.  # noqa: E501


        :return: The aws of this ProviderOptions.  # noqa: E501
        :rtype: ProviderOptionsAws
        """
        return self._aws

    @aws.setter
    def aws(self, aws):
        """Sets the aws of this ProviderOptions.


        :param aws: The aws of this ProviderOptions.  # noqa: E501
        :type: ProviderOptionsAws
        """

        self._aws = aws

    @property
    def aws_govcloud(self):
        """Gets the aws_govcloud of this ProviderOptions.  # noqa: E501


        :return: The aws_govcloud of this ProviderOptions.  # noqa: E501
        :rtype: ProviderOptionsAws
        """
        return self._aws_govcloud

    @aws_govcloud.setter
    def aws_govcloud(self, aws_govcloud):
        """Sets the aws_govcloud of this ProviderOptions.


        :param aws_govcloud: The aws_govcloud of this ProviderOptions.  # noqa: E501
        :type: ProviderOptionsAws
        """

        self._aws_govcloud = aws_govcloud

    @property
    def azure(self):
        """Gets the azure of this ProviderOptions.  # noqa: E501


        :return: The azure of this ProviderOptions.  # noqa: E501
        :rtype: ProviderOptionsAzure
        """
        return self._azure

    @azure.setter
    def azure(self, azure):
        """Sets the azure of this ProviderOptions.


        :param azure: The azure of this ProviderOptions.  # noqa: E501
        :type: ProviderOptionsAzure
        """

        self._azure = azure

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ProviderOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other