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


class ImageVulnResponseFacade(object):
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
        'details': 'list[ServiceVulnerabilityDetails]',
        'vuln_summary': 'VulnSummary'
    }

    attribute_map = {
        'details': 'details',
        'vuln_summary': 'vulnSummary'
    }

    def __init__(self, details=None, vuln_summary=None, local_vars_configuration=None):  # noqa: E501
        """ImageVulnResponseFacade - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._details = None
        self._vuln_summary = None
        self.discriminator = None

        if details is not None:
            self.details = details
        if vuln_summary is not None:
            self.vuln_summary = vuln_summary

    @property
    def details(self):
        """Gets the details of this ImageVulnResponseFacade.  # noqa: E501


        :return: The details of this ImageVulnResponseFacade.  # noqa: E501
        :rtype: list[ServiceVulnerabilityDetails]
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this ImageVulnResponseFacade.


        :param details: The details of this ImageVulnResponseFacade.  # noqa: E501
        :type: list[ServiceVulnerabilityDetails]
        """

        self._details = details

    @property
    def vuln_summary(self):
        """Gets the vuln_summary of this ImageVulnResponseFacade.  # noqa: E501


        :return: The vuln_summary of this ImageVulnResponseFacade.  # noqa: E501
        :rtype: VulnSummary
        """
        return self._vuln_summary

    @vuln_summary.setter
    def vuln_summary(self, vuln_summary):
        """Sets the vuln_summary of this ImageVulnResponseFacade.


        :param vuln_summary: The vuln_summary of this ImageVulnResponseFacade.  # noqa: E501
        :type: VulnSummary
        """

        self._vuln_summary = vuln_summary

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
        if not isinstance(other, ImageVulnResponseFacade):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ImageVulnResponseFacade):
            return True

        return self.to_dict() != other.to_dict()
