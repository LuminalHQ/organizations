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

from swagger_client.models.event import Event  # noqa: F401,E501


class Events(object):
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
        'items': 'list[Event]',
        'is_truncated': 'bool',
        'next_offset': 'int',
        'count': 'int'
    }

    attribute_map = {
        'items': 'items',
        'is_truncated': 'is_truncated',
        'next_offset': 'next_offset',
        'count': 'count'
    }

    def __init__(self, items=None, is_truncated=None, next_offset=None, count=None):  # noqa: E501
        """Events - a model defined in Swagger"""  # noqa: E501

        self._items = None
        self._is_truncated = None
        self._next_offset = None
        self._count = None
        self.discriminator = None

        if items is not None:
            self.items = items
        if is_truncated is not None:
            self.is_truncated = is_truncated
        if next_offset is not None:
            self.next_offset = next_offset
        if count is not None:
            self.count = count

    @property
    def items(self):
        """Gets the items of this Events.  # noqa: E501

        Paginated list of events.  # noqa: E501

        :return: The items of this Events.  # noqa: E501
        :rtype: list[Event]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this Events.

        Paginated list of events.  # noqa: E501

        :param items: The items of this Events.  # noqa: E501
        :type: list[Event]
        """

        self._items = items

    @property
    def is_truncated(self):
        """Gets the is_truncated of this Events.  # noqa: E501

        Indicates whether there are more items at the next offset.  # noqa: E501

        :return: The is_truncated of this Events.  # noqa: E501
        :rtype: bool
        """
        return self._is_truncated

    @is_truncated.setter
    def is_truncated(self, is_truncated):
        """Sets the is_truncated of this Events.

        Indicates whether there are more items at the next offset.  # noqa: E501

        :param is_truncated: The is_truncated of this Events.  # noqa: E501
        :type: bool
        """

        self._is_truncated = is_truncated

    @property
    def next_offset(self):
        """Gets the next_offset of this Events.  # noqa: E501

        Next offset to use to get the next page of items.  # noqa: E501

        :return: The next_offset of this Events.  # noqa: E501
        :rtype: int
        """
        return self._next_offset

    @next_offset.setter
    def next_offset(self, next_offset):
        """Sets the next_offset of this Events.

        Next offset to use to get the next page of items.  # noqa: E501

        :param next_offset: The next_offset of this Events.  # noqa: E501
        :type: int
        """

        self._next_offset = next_offset

    @property
    def count(self):
        """Gets the count of this Events.  # noqa: E501

        Total number of items. DEPRECATED: This property no longer returns accurate counts when filters are applied and will be removed in future API versions  # noqa: E501

        :return: The count of this Events.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this Events.

        Total number of items. DEPRECATED: This property no longer returns accurate counts when filters are applied and will be removed in future API versions  # noqa: E501

        :param count: The count of this Events.  # noqa: E501
        :type: int
        """

        self._count = count

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
        if not isinstance(other, Events):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
