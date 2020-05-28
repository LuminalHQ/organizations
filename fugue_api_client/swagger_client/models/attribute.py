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


class Attribute(object):
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
        'name': 'str',
        'attr_type': 'str',
        'old': 'str',
        'new': 'str',
        'removed': 'bool',
        'requires_new': 'bool',
        'sensitive': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'attr_type': 'attr_type',
        'old': 'old',
        'new': 'new',
        'removed': 'removed',
        'requires_new': 'requires_new',
        'sensitive': 'sensitive'
    }

    def __init__(self, name=None, attr_type=None, old=None, new=None, removed=None, requires_new=None, sensitive=None):  # noqa: E501
        """Attribute - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._attr_type = None
        self._old = None
        self._new = None
        self._removed = None
        self._requires_new = None
        self._sensitive = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if attr_type is not None:
            self.attr_type = attr_type
        if old is not None:
            self.old = old
        if new is not None:
            self.new = new
        if removed is not None:
            self.removed = removed
        if requires_new is not None:
            self.requires_new = requires_new
        if sensitive is not None:
            self.sensitive = sensitive

    @property
    def name(self):
        """Gets the name of this Attribute.  # noqa: E501

        Name of the attribute.  # noqa: E501

        :return: The name of this Attribute.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Attribute.

        Name of the attribute.  # noqa: E501

        :param name: The name of this Attribute.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def attr_type(self):
        """Gets the attr_type of this Attribute.  # noqa: E501

        Indicates whether the attribute type is input or output.  # noqa: E501

        :return: The attr_type of this Attribute.  # noqa: E501
        :rtype: str
        """
        return self._attr_type

    @attr_type.setter
    def attr_type(self, attr_type):
        """Sets the attr_type of this Attribute.

        Indicates whether the attribute type is input or output.  # noqa: E501

        :param attr_type: The attr_type of this Attribute.  # noqa: E501
        :type: str
        """

        self._attr_type = attr_type

    @property
    def old(self):
        """Gets the old of this Attribute.  # noqa: E501

        Value of the attribute before the event.  # noqa: E501

        :return: The old of this Attribute.  # noqa: E501
        :rtype: str
        """
        return self._old

    @old.setter
    def old(self, old):
        """Sets the old of this Attribute.

        Value of the attribute before the event.  # noqa: E501

        :param old: The old of this Attribute.  # noqa: E501
        :type: str
        """

        self._old = old

    @property
    def new(self):
        """Gets the new of this Attribute.  # noqa: E501

        Value of the attribute as a result of the event.  # noqa: E501

        :return: The new of this Attribute.  # noqa: E501
        :rtype: str
        """
        return self._new

    @new.setter
    def new(self, new):
        """Sets the new of this Attribute.

        Value of the attribute as a result of the event.  # noqa: E501

        :param new: The new of this Attribute.  # noqa: E501
        :type: str
        """

        self._new = new

    @property
    def removed(self):
        """Gets the removed of this Attribute.  # noqa: E501

        Indicates whether the attribute was removed.  # noqa: E501

        :return: The removed of this Attribute.  # noqa: E501
        :rtype: bool
        """
        return self._removed

    @removed.setter
    def removed(self, removed):
        """Sets the removed of this Attribute.

        Indicates whether the attribute was removed.  # noqa: E501

        :param removed: The removed of this Attribute.  # noqa: E501
        :type: bool
        """

        self._removed = removed

    @property
    def requires_new(self):
        """Gets the requires_new of this Attribute.  # noqa: E501

        Indicates whether the attribute needed to be deleted and recreated.  # noqa: E501

        :return: The requires_new of this Attribute.  # noqa: E501
        :rtype: bool
        """
        return self._requires_new

    @requires_new.setter
    def requires_new(self, requires_new):
        """Sets the requires_new of this Attribute.

        Indicates whether the attribute needed to be deleted and recreated.  # noqa: E501

        :param requires_new: The requires_new of this Attribute.  # noqa: E501
        :type: bool
        """

        self._requires_new = requires_new

    @property
    def sensitive(self):
        """Gets the sensitive of this Attribute.  # noqa: E501

        Indicates whether the attribute contains sensitive data.  # noqa: E501

        :return: The sensitive of this Attribute.  # noqa: E501
        :rtype: bool
        """
        return self._sensitive

    @sensitive.setter
    def sensitive(self, sensitive):
        """Sets the sensitive of this Attribute.

        Indicates whether the attribute contains sensitive data.  # noqa: E501

        :param sensitive: The sensitive of this Attribute.  # noqa: E501
        :type: bool
        """

        self._sensitive = sensitive

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
        if not isinstance(other, Attribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other