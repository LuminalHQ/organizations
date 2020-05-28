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


class ResourceTypeMetadata(object):
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
        'resource_types': 'list[str]',
        'recommended_types': 'list[str]'
    }

    attribute_map = {
        'resource_types': 'resource_types',
        'recommended_types': 'recommended_types'
    }

    def __init__(self, resource_types=None, recommended_types=None):  # noqa: E501
        """ResourceTypeMetadata - a model defined in Swagger"""  # noqa: E501

        self._resource_types = None
        self._recommended_types = None
        self.discriminator = None

        if resource_types is not None:
            self.resource_types = resource_types
        if recommended_types is not None:
            self.recommended_types = recommended_types

    @property
    def resource_types(self):
        """Gets the resource_types of this ResourceTypeMetadata.  # noqa: E501

        List of resource types supported by Fugue.  # noqa: E501

        :return: The resource_types of this ResourceTypeMetadata.  # noqa: E501
        :rtype: list[str]
        """
        return self._resource_types

    @resource_types.setter
    def resource_types(self, resource_types):
        """Sets the resource_types of this ResourceTypeMetadata.

        List of resource types supported by Fugue.  # noqa: E501

        :param resource_types: The resource_types of this ResourceTypeMetadata.  # noqa: E501
        :type: list[str]
        """

        self._resource_types = resource_types

    @property
    def recommended_types(self):
        """Gets the recommended_types of this ResourceTypeMetadata.  # noqa: E501

        List of Fugue recommended resource types.  # noqa: E501

        :return: The recommended_types of this ResourceTypeMetadata.  # noqa: E501
        :rtype: list[str]
        """
        return self._recommended_types

    @recommended_types.setter
    def recommended_types(self, recommended_types):
        """Sets the recommended_types of this ResourceTypeMetadata.

        List of Fugue recommended resource types.  # noqa: E501

        :param recommended_types: The recommended_types of this ResourceTypeMetadata.  # noqa: E501
        :type: list[str]
        """

        self._recommended_types = recommended_types

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
        if not isinstance(other, ResourceTypeMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
