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


class ContainerDeleteRequest(object):
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
        'container_ids': 'list[str]',
        'filter': 'str'
    }

    attribute_map = {
        'container_ids': 'containerIds',
        'filter': 'filter'
    }

    def __init__(self, container_ids=None, filter=None, local_vars_configuration=None):  # noqa: E501
        """ContainerDeleteRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._container_ids = None
        self._filter = None
        self.discriminator = None

        if container_ids is not None:
            self.container_ids = container_ids
        if filter is not None:
            self.filter = filter

    @property
    def container_ids(self):
        """Gets the container_ids of this ContainerDeleteRequest.  # noqa: E501


        :return: The container_ids of this ContainerDeleteRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._container_ids

    @container_ids.setter
    def container_ids(self, container_ids):
        """Sets the container_ids of this ContainerDeleteRequest.


        :param container_ids: The container_ids of this ContainerDeleteRequest.  # noqa: E501
        :type: list[str]
        """

        self._container_ids = container_ids

    @property
    def filter(self):
        """Gets the filter of this ContainerDeleteRequest.  # noqa: E501


        :return: The filter of this ContainerDeleteRequest.  # noqa: E501
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this ContainerDeleteRequest.


        :param filter: The filter of this ContainerDeleteRequest.  # noqa: E501
        :type: str
        """

        self._filter = filter

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
        if not isinstance(other, ContainerDeleteRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ContainerDeleteRequest):
            return True

        return self.to_dict() != other.to_dict()
