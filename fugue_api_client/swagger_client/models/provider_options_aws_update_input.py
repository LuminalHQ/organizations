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


class ProviderOptionsAwsUpdateInput(object):
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
        'role_arn': 'str',
        'regions': 'list[str]'
    }

    attribute_map = {
        'role_arn': 'role_arn',
        'regions': 'regions'
    }

    def __init__(self, role_arn=None, regions=None):  # noqa: E501
        """ProviderOptionsAwsUpdateInput - a model defined in Swagger"""  # noqa: E501

        self._role_arn = None
        self._regions = None
        self.discriminator = None

        if role_arn is not None:
            self.role_arn = role_arn
        if regions is not None:
            self.regions = regions

    @property
    def role_arn(self):
        """Gets the role_arn of this ProviderOptionsAwsUpdateInput.  # noqa: E501

        AWS IAM Role ARN that will be assumed to scan and remediate infrastructure.  # noqa: E501

        :return: The role_arn of this ProviderOptionsAwsUpdateInput.  # noqa: E501
        :rtype: str
        """
        return self._role_arn

    @role_arn.setter
    def role_arn(self, role_arn):
        """Sets the role_arn of this ProviderOptionsAwsUpdateInput.

        AWS IAM Role ARN that will be assumed to scan and remediate infrastructure.  # noqa: E501

        :param role_arn: The role_arn of this ProviderOptionsAwsUpdateInput.  # noqa: E501
        :type: str
        """

        self._role_arn = role_arn

    @property
    def regions(self):
        """Gets the regions of this ProviderOptionsAwsUpdateInput.  # noqa: E501

        The AWS regions to scan and remediate infrastructure in.  # noqa: E501

        :return: The regions of this ProviderOptionsAwsUpdateInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._regions

    @regions.setter
    def regions(self, regions):
        """Sets the regions of this ProviderOptionsAwsUpdateInput.

        The AWS regions to scan and remediate infrastructure in.  # noqa: E501

        :param regions: The regions of this ProviderOptionsAwsUpdateInput.  # noqa: E501
        :type: list[str]
        """

        self._regions = regions

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
        if not isinstance(other, ProviderOptionsAwsUpdateInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
