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


class VulnSummary(object):
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
        'confirmed': 'dict(str, int)',
        'patch_availability': 'PatchAvailability',
        'potential': 'dict(str, int)'
    }

    attribute_map = {
        'confirmed': 'confirmed',
        'patch_availability': 'patchAvailability',
        'potential': 'potential'
    }

    def __init__(self, confirmed=None, patch_availability=None, potential=None, local_vars_configuration=None):  # noqa: E501
        """VulnSummary - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._confirmed = None
        self._patch_availability = None
        self._potential = None
        self.discriminator = None

        if confirmed is not None:
            self.confirmed = confirmed
        if patch_availability is not None:
            self.patch_availability = patch_availability
        if potential is not None:
            self.potential = potential

    @property
    def confirmed(self):
        """Gets the confirmed of this VulnSummary.  # noqa: E501


        :return: The confirmed of this VulnSummary.  # noqa: E501
        :rtype: dict(str, int)
        """
        return self._confirmed

    @confirmed.setter
    def confirmed(self, confirmed):
        """Sets the confirmed of this VulnSummary.


        :param confirmed: The confirmed of this VulnSummary.  # noqa: E501
        :type: dict(str, int)
        """

        self._confirmed = confirmed

    @property
    def patch_availability(self):
        """Gets the patch_availability of this VulnSummary.  # noqa: E501


        :return: The patch_availability of this VulnSummary.  # noqa: E501
        :rtype: PatchAvailability
        """
        return self._patch_availability

    @patch_availability.setter
    def patch_availability(self, patch_availability):
        """Sets the patch_availability of this VulnSummary.


        :param patch_availability: The patch_availability of this VulnSummary.  # noqa: E501
        :type: PatchAvailability
        """

        self._patch_availability = patch_availability

    @property
    def potential(self):
        """Gets the potential of this VulnSummary.  # noqa: E501


        :return: The potential of this VulnSummary.  # noqa: E501
        :rtype: dict(str, int)
        """
        return self._potential

    @potential.setter
    def potential(self, potential):
        """Sets the potential of this VulnSummary.


        :param potential: The potential of this VulnSummary.  # noqa: E501
        :type: dict(str, int)
        """

        self._potential = potential

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
        if not isinstance(other, VulnSummary):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VulnSummary):
            return True

        return self.to_dict() != other.to_dict()
