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


class Layer(object):
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
        'comment': 'str',
        'created': 'str',
        'created_by': 'str',
        'id': 'str',
        'sha': 'str',
        'size': 'str',
        'tags': 'list[str]'
    }

    attribute_map = {
        'comment': 'comment',
        'created': 'created',
        'created_by': 'createdBy',
        'id': 'id',
        'sha': 'sha',
        'size': 'size',
        'tags': 'tags'
    }

    def __init__(self, comment=None, created=None, created_by=None, id=None, sha=None, size=None, tags=None, local_vars_configuration=None):  # noqa: E501
        """Layer - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._comment = None
        self._created = None
        self._created_by = None
        self._id = None
        self._sha = None
        self._size = None
        self._tags = None
        self.discriminator = None

        if comment is not None:
            self.comment = comment
        if created is not None:
            self.created = created
        if created_by is not None:
            self.created_by = created_by
        if id is not None:
            self.id = id
        if sha is not None:
            self.sha = sha
        if size is not None:
            self.size = size
        if tags is not None:
            self.tags = tags

    @property
    def comment(self):
        """Gets the comment of this Layer.  # noqa: E501


        :return: The comment of this Layer.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this Layer.


        :param comment: The comment of this Layer.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def created(self):
        """Gets the created of this Layer.  # noqa: E501


        :return: The created of this Layer.  # noqa: E501
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Layer.


        :param created: The created of this Layer.  # noqa: E501
        :type: str
        """

        self._created = created

    @property
    def created_by(self):
        """Gets the created_by of this Layer.  # noqa: E501


        :return: The created_by of this Layer.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Layer.


        :param created_by: The created_by of this Layer.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def id(self):
        """Gets the id of this Layer.  # noqa: E501


        :return: The id of this Layer.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Layer.


        :param id: The id of this Layer.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def sha(self):
        """Gets the sha of this Layer.  # noqa: E501


        :return: The sha of this Layer.  # noqa: E501
        :rtype: str
        """
        return self._sha

    @sha.setter
    def sha(self, sha):
        """Sets the sha of this Layer.


        :param sha: The sha of this Layer.  # noqa: E501
        :type: str
        """

        self._sha = sha

    @property
    def size(self):
        """Gets the size of this Layer.  # noqa: E501


        :return: The size of this Layer.  # noqa: E501
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this Layer.


        :param size: The size of this Layer.  # noqa: E501
        :type: str
        """

        self._size = size

    @property
    def tags(self):
        """Gets the tags of this Layer.  # noqa: E501


        :return: The tags of this Layer.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Layer.


        :param tags: The tags of this Layer.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

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
        if not isinstance(other, Layer):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Layer):
            return True

        return self.to_dict() != other.to_dict()
