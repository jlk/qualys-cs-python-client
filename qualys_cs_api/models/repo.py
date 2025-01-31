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


class Repo(object):
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
        'registry': 'str',
        'repository': 'str',
        'tag': 'str'
    }

    attribute_map = {
        'registry': 'registry',
        'repository': 'repository',
        'tag': 'tag'
    }

    def __init__(self, registry=None, repository=None, tag=None, local_vars_configuration=None):  # noqa: E501
        """Repo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._registry = None
        self._repository = None
        self._tag = None
        self.discriminator = None

        if registry is not None:
            self.registry = registry
        if repository is not None:
            self.repository = repository
        if tag is not None:
            self.tag = tag

    @property
    def registry(self):
        """Gets the registry of this Repo.  # noqa: E501


        :return: The registry of this Repo.  # noqa: E501
        :rtype: str
        """
        return self._registry

    @registry.setter
    def registry(self, registry):
        """Sets the registry of this Repo.


        :param registry: The registry of this Repo.  # noqa: E501
        :type: str
        """

        self._registry = registry

    @property
    def repository(self):
        """Gets the repository of this Repo.  # noqa: E501


        :return: The repository of this Repo.  # noqa: E501
        :rtype: str
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        """Sets the repository of this Repo.


        :param repository: The repository of this Repo.  # noqa: E501
        :type: str
        """

        self._repository = repository

    @property
    def tag(self):
        """Gets the tag of this Repo.  # noqa: E501


        :return: The tag of this Repo.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this Repo.


        :param tag: The tag of this Repo.  # noqa: E501
        :type: str
        """

        self._tag = tag

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
        if not isinstance(other, Repo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Repo):
            return True

        return self.to_dict() != other.to_dict()
