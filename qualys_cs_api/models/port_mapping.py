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


class PortMapping(object):
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
        'host_ip': 'str',
        'host_port': 'int',
        'port': 'int',
        'protocol': 'str'
    }

    attribute_map = {
        'host_ip': 'hostIp',
        'host_port': 'hostPort',
        'port': 'port',
        'protocol': 'protocol'
    }

    def __init__(self, host_ip=None, host_port=None, port=None, protocol=None, local_vars_configuration=None):  # noqa: E501
        """PortMapping - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._host_ip = None
        self._host_port = None
        self._port = None
        self._protocol = None
        self.discriminator = None

        if host_ip is not None:
            self.host_ip = host_ip
        if host_port is not None:
            self.host_port = host_port
        if port is not None:
            self.port = port
        if protocol is not None:
            self.protocol = protocol

    @property
    def host_ip(self):
        """Gets the host_ip of this PortMapping.  # noqa: E501


        :return: The host_ip of this PortMapping.  # noqa: E501
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        """Sets the host_ip of this PortMapping.


        :param host_ip: The host_ip of this PortMapping.  # noqa: E501
        :type: str
        """

        self._host_ip = host_ip

    @property
    def host_port(self):
        """Gets the host_port of this PortMapping.  # noqa: E501


        :return: The host_port of this PortMapping.  # noqa: E501
        :rtype: int
        """
        return self._host_port

    @host_port.setter
    def host_port(self, host_port):
        """Sets the host_port of this PortMapping.


        :param host_port: The host_port of this PortMapping.  # noqa: E501
        :type: int
        """

        self._host_port = host_port

    @property
    def port(self):
        """Gets the port of this PortMapping.  # noqa: E501


        :return: The port of this PortMapping.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this PortMapping.


        :param port: The port of this PortMapping.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def protocol(self):
        """Gets the protocol of this PortMapping.  # noqa: E501


        :return: The protocol of this PortMapping.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this PortMapping.


        :param protocol: The protocol of this PortMapping.  # noqa: E501
        :type: str
        """

        self._protocol = protocol

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
        if not isinstance(other, PortMapping):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PortMapping):
            return True

        return self.to_dict() != other.to_dict()
