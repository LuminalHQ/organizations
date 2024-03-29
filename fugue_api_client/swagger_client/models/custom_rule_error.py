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


class CustomRuleError(object):
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
        'severity': 'str',
        'text': 'str'
    }

    attribute_map = {
        'severity': 'severity',
        'text': 'text'
    }

    def __init__(self, severity=None, text=None):  # noqa: E501
        """CustomRuleError - a model defined in Swagger"""  # noqa: E501

        self._severity = None
        self._text = None
        self.discriminator = None

        if severity is not None:
            self.severity = severity
        if text is not None:
            self.text = text

    @property
    def severity(self):
        """Gets the severity of this CustomRuleError.  # noqa: E501

        Severity of the error.  # noqa: E501

        :return: The severity of this CustomRuleError.  # noqa: E501
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this CustomRuleError.

        Severity of the error.  # noqa: E501

        :param severity: The severity of this CustomRuleError.  # noqa: E501
        :type: str
        """
        allowed_values = ["error", "warning"]  # noqa: E501
        if severity not in allowed_values:
            raise ValueError(
                "Invalid value for `severity` ({0}), must be one of {1}"  # noqa: E501
                .format(severity, allowed_values)
            )

        self._severity = severity

    @property
    def text(self):
        """Gets the text of this CustomRuleError.  # noqa: E501

        Text describing the error  # noqa: E501

        :return: The text of this CustomRuleError.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this CustomRuleError.

        Text describing the error  # noqa: E501

        :param text: The text of this CustomRuleError.  # noqa: E501
        :type: str
        """

        self._text = text

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
        if not isinstance(other, CustomRuleError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
