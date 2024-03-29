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


class ComplianceDiffRules(object):
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
        'summary': 'str',
        'old_state': 'str',
        'new_state': 'str',
        'old_message': 'str',
        'new_message': 'str',
        'compliance_families': 'list[str]',
        'controls': 'list[str]'
    }

    attribute_map = {
        'summary': 'summary',
        'old_state': 'old_state',
        'new_state': 'new_state',
        'old_message': 'old_message',
        'new_message': 'new_message',
        'compliance_families': 'compliance_families',
        'controls': 'controls'
    }

    def __init__(self, summary=None, old_state=None, new_state=None, old_message=None, new_message=None, compliance_families=None, controls=None):  # noqa: E501
        """ComplianceDiffRules - a model defined in Swagger"""  # noqa: E501

        self._summary = None
        self._old_state = None
        self._new_state = None
        self._old_message = None
        self._new_message = None
        self._compliance_families = None
        self._controls = None
        self.discriminator = None

        if summary is not None:
            self.summary = summary
        if old_state is not None:
            self.old_state = old_state
        if new_state is not None:
            self.new_state = new_state
        if old_message is not None:
            self.old_message = old_message
        if new_message is not None:
            self.new_message = new_message
        if compliance_families is not None:
            self.compliance_families = compliance_families
        if controls is not None:
            self.controls = controls

    @property
    def summary(self):
        """Gets the summary of this ComplianceDiffRules.  # noqa: E501

        Summary of the rule a resource was evaluated against.  # noqa: E501

        :return: The summary of this ComplianceDiffRules.  # noqa: E501
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this ComplianceDiffRules.

        Summary of the rule a resource was evaluated against.  # noqa: E501

        :param summary: The summary of this ComplianceDiffRules.  # noqa: E501
        :type: str
        """

        self._summary = summary

    @property
    def old_state(self):
        """Gets the old_state of this ComplianceDiffRules.  # noqa: E501

        The rule's evaluation state before an event.  # noqa: E501

        :return: The old_state of this ComplianceDiffRules.  # noqa: E501
        :rtype: str
        """
        return self._old_state

    @old_state.setter
    def old_state(self, old_state):
        """Sets the old_state of this ComplianceDiffRules.

        The rule's evaluation state before an event.  # noqa: E501

        :param old_state: The old_state of this ComplianceDiffRules.  # noqa: E501
        :type: str
        """

        self._old_state = old_state

    @property
    def new_state(self):
        """Gets the new_state of this ComplianceDiffRules.  # noqa: E501

        The rule's evaluation state after an event.  # noqa: E501

        :return: The new_state of this ComplianceDiffRules.  # noqa: E501
        :rtype: str
        """
        return self._new_state

    @new_state.setter
    def new_state(self, new_state):
        """Sets the new_state of this ComplianceDiffRules.

        The rule's evaluation state after an event.  # noqa: E501

        :param new_state: The new_state of this ComplianceDiffRules.  # noqa: E501
        :type: str
        """

        self._new_state = new_state

    @property
    def old_message(self):
        """Gets the old_message of this ComplianceDiffRules.  # noqa: E501

        The rule's error message before an event.  # noqa: E501

        :return: The old_message of this ComplianceDiffRules.  # noqa: E501
        :rtype: str
        """
        return self._old_message

    @old_message.setter
    def old_message(self, old_message):
        """Sets the old_message of this ComplianceDiffRules.

        The rule's error message before an event.  # noqa: E501

        :param old_message: The old_message of this ComplianceDiffRules.  # noqa: E501
        :type: str
        """

        self._old_message = old_message

    @property
    def new_message(self):
        """Gets the new_message of this ComplianceDiffRules.  # noqa: E501

        The rule's error message after an event.  # noqa: E501

        :return: The new_message of this ComplianceDiffRules.  # noqa: E501
        :rtype: str
        """
        return self._new_message

    @new_message.setter
    def new_message(self, new_message):
        """Sets the new_message of this ComplianceDiffRules.

        The rule's error message after an event.  # noqa: E501

        :param new_message: The new_message of this ComplianceDiffRules.  # noqa: E501
        :type: str
        """

        self._new_message = new_message

    @property
    def compliance_families(self):
        """Gets the compliance_families of this ComplianceDiffRules.  # noqa: E501

        The compliance families that a rule is evaluated for.  # noqa: E501

        :return: The compliance_families of this ComplianceDiffRules.  # noqa: E501
        :rtype: list[str]
        """
        return self._compliance_families

    @compliance_families.setter
    def compliance_families(self, compliance_families):
        """Sets the compliance_families of this ComplianceDiffRules.

        The compliance families that a rule is evaluated for.  # noqa: E501

        :param compliance_families: The compliance_families of this ComplianceDiffRules.  # noqa: E501
        :type: list[str]
        """

        self._compliance_families = compliance_families

    @property
    def controls(self):
        """Gets the controls of this ComplianceDiffRules.  # noqa: E501

        The compliance controls that a rule is evaluated for.  # noqa: E501

        :return: The controls of this ComplianceDiffRules.  # noqa: E501
        :rtype: list[str]
        """
        return self._controls

    @controls.setter
    def controls(self, controls):
        """Sets the controls of this ComplianceDiffRules.

        The compliance controls that a rule is evaluated for.  # noqa: E501

        :param controls: The controls of this ComplianceDiffRules.  # noqa: E501
        :type: list[str]
        """

        self._controls = controls

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
        if not isinstance(other, ComplianceDiffRules):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
