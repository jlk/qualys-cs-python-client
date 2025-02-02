# coding: utf-8

"""
    Container Security APIs

    All features of the Container Security are available through REST APIs.<br/>Access support information at www.qualys.com/support/<br/><br/><b>Permissions:</b><br/>User must have the Container module enabled<br/>User must have API ACCESS permission  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from qualys_cs_api.configuration import Configuration


class Software(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'fix_version': 'str',
        'name': 'str',
        'version': 'str',
        'vulnerabilities': 'list[ServiceVulnerabilityDetails]'
    }

    attribute_map = {
        'fix_version': 'fixVersion',
        'name': 'name',
        'version': 'version',
        'vulnerabilities': 'vulnerabilities'
    }

    def __init__(self, fix_version=None, name=None, version=None, vulnerabilities=None, local_vars_configuration=None):  # noqa: E501
        """Software - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._fix_version = None
        self._name = None
        self._version = None
        self._vulnerabilities = None
        self.discriminator = None

        if fix_version is not None:
            self.fix_version = fix_version
        if name is not None:
            self.name = name
        if version is not None:
            self.version = version
        if vulnerabilities is not None:
            self.vulnerabilities = vulnerabilities

    @property
    def fix_version(self):
        """Gets the fix_version of this Software.  # noqa: E501


        :return: The fix_version of this Software.  # noqa: E501
        :rtype: str
        """
        return self._fix_version

    @fix_version.setter
    def fix_version(self, fix_version):
        """Sets the fix_version of this Software.


        :param fix_version: The fix_version of this Software.  # noqa: E501
        :type: str
        """

        self._fix_version = fix_version

    @property
    def name(self):
        """Gets the name of this Software.  # noqa: E501


        :return: The name of this Software.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Software.


        :param name: The name of this Software.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def version(self):
        """Gets the version of this Software.  # noqa: E501


        :return: The version of this Software.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Software.


        :param version: The version of this Software.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def vulnerabilities(self):
        """Gets the vulnerabilities of this Software.  # noqa: E501


        :return: The vulnerabilities of this Software.  # noqa: E501
        :rtype: list[ServiceVulnerabilityDetails]
        """
        return self._vulnerabilities

    @vulnerabilities.setter
    def vulnerabilities(self, vulnerabilities):
        """Sets the vulnerabilities of this Software.


        :param vulnerabilities: The vulnerabilities of this Software.  # noqa: E501
        :type: list[ServiceVulnerabilityDetails]
        """

        self._vulnerabilities = vulnerabilities

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, Software):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Software):
            return True

        return self.to_dict() != other.to_dict()
