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


class CMSError(object):
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
        'context_params': 'object',
        'error_code': 'str',
        'error_message': 'str'
    }

    attribute_map = {
        'context_params': 'contextParams',
        'error_code': 'errorCode',
        'error_message': 'errorMessage'
    }

    def __init__(self, context_params=None, error_code=None, error_message=None, local_vars_configuration=None):  # noqa: E501
        """CMSError - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._context_params = None
        self._error_code = None
        self._error_message = None
        self.discriminator = None

        if context_params is not None:
            self.context_params = context_params
        if error_code is not None:
            self.error_code = error_code
        if error_message is not None:
            self.error_message = error_message

    @property
    def context_params(self):
        """Gets the context_params of this CMSError.  # noqa: E501


        :return: The context_params of this CMSError.  # noqa: E501
        :rtype: object
        """
        return self._context_params

    @context_params.setter
    def context_params(self, context_params):
        """Sets the context_params of this CMSError.


        :param context_params: The context_params of this CMSError.  # noqa: E501
        :type: object
        """

        self._context_params = context_params

    @property
    def error_code(self):
        """Gets the error_code of this CMSError.  # noqa: E501


        :return: The error_code of this CMSError.  # noqa: E501
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this CMSError.


        :param error_code: The error_code of this CMSError.  # noqa: E501
        :type: str
        """

        self._error_code = error_code

    @property
    def error_message(self):
        """Gets the error_message of this CMSError.  # noqa: E501


        :return: The error_message of this CMSError.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this CMSError.


        :param error_message: The error_message of this CMSError.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

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
        if not isinstance(other, CMSError):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CMSError):
            return True

        return self.to_dict() != other.to_dict()
