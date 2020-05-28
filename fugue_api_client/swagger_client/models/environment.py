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

from swagger_client.models.provider_options import ProviderOptions  # noqa: F401,E501


class Environment(object):
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
        'id': 'str',
        'tenant_id': 'str',
        'name': 'str',
        'provider': 'str',
        'provider_options': 'ProviderOptions',
        'compliance_families': 'list[str]',
        'baseline_id': 'str',
        'drift': 'bool',
        'remediation': 'bool',
        'scan_status': 'str',
        'scan_interval': 'int',
        'last_scan_at': 'int',
        'next_scan_at': 'int',
        'survey_resource_types': 'list[str]',
        'remediate_resource_types': 'list[str]',
        'scan_schedule_enabled': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'tenant_id': 'tenant_id',
        'name': 'name',
        'provider': 'provider',
        'provider_options': 'provider_options',
        'compliance_families': 'compliance_families',
        'baseline_id': 'baseline_id',
        'drift': 'drift',
        'remediation': 'remediation',
        'scan_status': 'scan_status',
        'scan_interval': 'scan_interval',
        'last_scan_at': 'last_scan_at',
        'next_scan_at': 'next_scan_at',
        'survey_resource_types': 'survey_resource_types',
        'remediate_resource_types': 'remediate_resource_types',
        'scan_schedule_enabled': 'scan_schedule_enabled'
    }

    def __init__(self, id=None, tenant_id=None, name=None, provider=None, provider_options=None, compliance_families=None, baseline_id=None, drift=None, remediation=None, scan_status=None, scan_interval=None, last_scan_at=None, next_scan_at=None, survey_resource_types=None, remediate_resource_types=None, scan_schedule_enabled=None):  # noqa: E501
        """Environment - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._tenant_id = None
        self._name = None
        self._provider = None
        self._provider_options = None
        self._compliance_families = None
        self._baseline_id = None
        self._drift = None
        self._remediation = None
        self._scan_status = None
        self._scan_interval = None
        self._last_scan_at = None
        self._next_scan_at = None
        self._survey_resource_types = None
        self._remediate_resource_types = None
        self._scan_schedule_enabled = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if name is not None:
            self.name = name
        if provider is not None:
            self.provider = provider
        if provider_options is not None:
            self.provider_options = provider_options
        if compliance_families is not None:
            self.compliance_families = compliance_families
        if baseline_id is not None:
            self.baseline_id = baseline_id
        if drift is not None:
            self.drift = drift
        if remediation is not None:
            self.remediation = remediation
        if scan_status is not None:
            self.scan_status = scan_status
        if scan_interval is not None:
            self.scan_interval = scan_interval
        if last_scan_at is not None:
            self.last_scan_at = last_scan_at
        if next_scan_at is not None:
            self.next_scan_at = next_scan_at
        if survey_resource_types is not None:
            self.survey_resource_types = survey_resource_types
        if remediate_resource_types is not None:
            self.remediate_resource_types = remediate_resource_types
        if scan_schedule_enabled is not None:
            self.scan_schedule_enabled = scan_schedule_enabled

    @property
    def id(self):
        """Gets the id of this Environment.  # noqa: E501

        ID of the environment.  # noqa: E501

        :return: The id of this Environment.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Environment.

        ID of the environment.  # noqa: E501

        :param id: The id of this Environment.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def tenant_id(self):
        """Gets the tenant_id of this Environment.  # noqa: E501

        ID of the tenant that owns the environment.  # noqa: E501

        :return: The tenant_id of this Environment.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this Environment.

        ID of the tenant that owns the environment.  # noqa: E501

        :param tenant_id: The tenant_id of this Environment.  # noqa: E501
        :type: str
        """

        self._tenant_id = tenant_id

    @property
    def name(self):
        """Gets the name of this Environment.  # noqa: E501

        Name of the environment.  # noqa: E501

        :return: The name of this Environment.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Environment.

        Name of the environment.  # noqa: E501

        :param name: The name of this Environment.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def provider(self):
        """Gets the provider of this Environment.  # noqa: E501

        Name of the cloud service provider for the environment.  # noqa: E501

        :return: The provider of this Environment.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this Environment.

        Name of the cloud service provider for the environment.  # noqa: E501

        :param provider: The provider of this Environment.  # noqa: E501
        :type: str
        """
        allowed_values = ["aws", "aws_govcloud", "azure"]  # noqa: E501
        if provider not in allowed_values:
            raise ValueError(
                "Invalid value for `provider` ({0}), must be one of {1}"  # noqa: E501
                .format(provider, allowed_values)
            )

        self._provider = provider

    @property
    def provider_options(self):
        """Gets the provider_options of this Environment.  # noqa: E501


        :return: The provider_options of this Environment.  # noqa: E501
        :rtype: ProviderOptions
        """
        return self._provider_options

    @provider_options.setter
    def provider_options(self, provider_options):
        """Sets the provider_options of this Environment.


        :param provider_options: The provider_options of this Environment.  # noqa: E501
        :type: ProviderOptions
        """

        self._provider_options = provider_options

    @property
    def compliance_families(self):
        """Gets the compliance_families of this Environment.  # noqa: E501

        List of compliance families validated against the environment.  # noqa: E501

        :return: The compliance_families of this Environment.  # noqa: E501
        :rtype: list[str]
        """
        return self._compliance_families

    @compliance_families.setter
    def compliance_families(self, compliance_families):
        """Sets the compliance_families of this Environment.

        List of compliance families validated against the environment.  # noqa: E501

        :param compliance_families: The compliance_families of this Environment.  # noqa: E501
        :type: list[str]
        """

        self._compliance_families = compliance_families

    @property
    def baseline_id(self):
        """Gets the baseline_id of this Environment.  # noqa: E501

        Scan ID of the baseline if baseline is enabled.  # noqa: E501

        :return: The baseline_id of this Environment.  # noqa: E501
        :rtype: str
        """
        return self._baseline_id

    @baseline_id.setter
    def baseline_id(self, baseline_id):
        """Sets the baseline_id of this Environment.

        Scan ID of the baseline if baseline is enabled.  # noqa: E501

        :param baseline_id: The baseline_id of this Environment.  # noqa: E501
        :type: str
        """

        self._baseline_id = baseline_id

    @property
    def drift(self):
        """Gets the drift of this Environment.  # noqa: E501

        Indicates whether drift detection is enabled for the environment.  # noqa: E501

        :return: The drift of this Environment.  # noqa: E501
        :rtype: bool
        """
        return self._drift

    @drift.setter
    def drift(self, drift):
        """Sets the drift of this Environment.

        Indicates whether drift detection is enabled for the environment.  # noqa: E501

        :param drift: The drift of this Environment.  # noqa: E501
        :type: bool
        """

        self._drift = drift

    @property
    def remediation(self):
        """Gets the remediation of this Environment.  # noqa: E501

        Indicates whether remediation is enabled for the environment.  # noqa: E501

        :return: The remediation of this Environment.  # noqa: E501
        :rtype: bool
        """
        return self._remediation

    @remediation.setter
    def remediation(self, remediation):
        """Sets the remediation of this Environment.

        Indicates whether remediation is enabled for the environment.  # noqa: E501

        :param remediation: The remediation of this Environment.  # noqa: E501
        :type: bool
        """

        self._remediation = remediation

    @property
    def scan_status(self):
        """Gets the scan_status of this Environment.  # noqa: E501

        Status of the current or most recently completed scan for the environment.  # noqa: E501

        :return: The scan_status of this Environment.  # noqa: E501
        :rtype: str
        """
        return self._scan_status

    @scan_status.setter
    def scan_status(self, scan_status):
        """Sets the scan_status of this Environment.

        Status of the current or most recently completed scan for the environment.  # noqa: E501

        :param scan_status: The scan_status of this Environment.  # noqa: E501
        :type: str
        """
        allowed_values = ["CREATED", "QUEUED", "IN_PROGRESS", "ERROR", "SUCCESS", "CANCELED"]  # noqa: E501
        if scan_status not in allowed_values:
            raise ValueError(
                "Invalid value for `scan_status` ({0}), must be one of {1}"  # noqa: E501
                .format(scan_status, allowed_values)
            )

        self._scan_status = scan_status

    @property
    def scan_interval(self):
        """Gets the scan_interval of this Environment.  # noqa: E501

        Time in seconds between the end of one scan to the start of the next.  # noqa: E501

        :return: The scan_interval of this Environment.  # noqa: E501
        :rtype: int
        """
        return self._scan_interval

    @scan_interval.setter
    def scan_interval(self, scan_interval):
        """Sets the scan_interval of this Environment.

        Time in seconds between the end of one scan to the start of the next.  # noqa: E501

        :param scan_interval: The scan_interval of this Environment.  # noqa: E501
        :type: int
        """

        self._scan_interval = scan_interval

    @property
    def last_scan_at(self):
        """Gets the last_scan_at of this Environment.  # noqa: E501

        Time the current or most recently completed scan for the environment started.  # noqa: E501

        :return: The last_scan_at of this Environment.  # noqa: E501
        :rtype: int
        """
        return self._last_scan_at

    @last_scan_at.setter
    def last_scan_at(self, last_scan_at):
        """Sets the last_scan_at of this Environment.

        Time the current or most recently completed scan for the environment started.  # noqa: E501

        :param last_scan_at: The last_scan_at of this Environment.  # noqa: E501
        :type: int
        """

        self._last_scan_at = last_scan_at

    @property
    def next_scan_at(self):
        """Gets the next_scan_at of this Environment.  # noqa: E501

        Time the next scan will start.  # noqa: E501

        :return: The next_scan_at of this Environment.  # noqa: E501
        :rtype: int
        """
        return self._next_scan_at

    @next_scan_at.setter
    def next_scan_at(self, next_scan_at):
        """Sets the next_scan_at of this Environment.

        Time the next scan will start.  # noqa: E501

        :param next_scan_at: The next_scan_at of this Environment.  # noqa: E501
        :type: int
        """

        self._next_scan_at = next_scan_at

    @property
    def survey_resource_types(self):
        """Gets the survey_resource_types of this Environment.  # noqa: E501

        List of resource types surveyed for the environment.  # noqa: E501

        :return: The survey_resource_types of this Environment.  # noqa: E501
        :rtype: list[str]
        """
        return self._survey_resource_types

    @survey_resource_types.setter
    def survey_resource_types(self, survey_resource_types):
        """Sets the survey_resource_types of this Environment.

        List of resource types surveyed for the environment.  # noqa: E501

        :param survey_resource_types: The survey_resource_types of this Environment.  # noqa: E501
        :type: list[str]
        """

        self._survey_resource_types = survey_resource_types

    @property
    def remediate_resource_types(self):
        """Gets the remediate_resource_types of this Environment.  # noqa: E501

        List of resource types remediated for the environment if remediation is enabled.  # noqa: E501

        :return: The remediate_resource_types of this Environment.  # noqa: E501
        :rtype: list[str]
        """
        return self._remediate_resource_types

    @remediate_resource_types.setter
    def remediate_resource_types(self, remediate_resource_types):
        """Sets the remediate_resource_types of this Environment.

        List of resource types remediated for the environment if remediation is enabled.  # noqa: E501

        :param remediate_resource_types: The remediate_resource_types of this Environment.  # noqa: E501
        :type: list[str]
        """

        self._remediate_resource_types = remediate_resource_types

    @property
    def scan_schedule_enabled(self):
        """Gets the scan_schedule_enabled of this Environment.  # noqa: E501

        Indicates whether the environment should have scans run on a schedule.  # noqa: E501

        :return: The scan_schedule_enabled of this Environment.  # noqa: E501
        :rtype: bool
        """
        return self._scan_schedule_enabled

    @scan_schedule_enabled.setter
    def scan_schedule_enabled(self, scan_schedule_enabled):
        """Sets the scan_schedule_enabled of this Environment.

        Indicates whether the environment should have scans run on a schedule.  # noqa: E501

        :param scan_schedule_enabled: The scan_schedule_enabled of this Environment.  # noqa: E501
        :type: bool
        """

        self._scan_schedule_enabled = scan_schedule_enabled

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
        if not isinstance(other, Environment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other