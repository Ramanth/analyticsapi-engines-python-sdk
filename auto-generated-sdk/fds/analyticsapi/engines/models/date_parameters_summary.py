# coding: utf-8

"""
    Engines API

    Allow clients to fetch Engines Analytics through APIs.  # noqa: E501

    The version of the OpenAPI document: 2
    Contact: analytics.api.support@factset.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from fds.analyticsapi.engines.configuration import Configuration


class DateParametersSummary(object):
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
        'startdate': 'str',
        'enddate': 'str'
    }

    attribute_map = {
        'startdate': 'startdate',
        'enddate': 'enddate'
    }

    def __init__(self, startdate=None, enddate=None, local_vars_configuration=None):  # noqa: E501
        """DateParametersSummary - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._startdate = None
        self._enddate = None
        self.discriminator = None

        if startdate is not None:
            self.startdate = startdate
        if enddate is not None:
            self.enddate = enddate

    @property
    def startdate(self):
        """Gets the startdate of this DateParametersSummary.  # noqa: E501

        Start date in YYYYMMDD format.  # noqa: E501

        :return: The startdate of this DateParametersSummary.  # noqa: E501
        :rtype: str
        """
        return self._startdate

    @startdate.setter
    def startdate(self, startdate):
        """Sets the startdate of this DateParametersSummary.

        Start date in YYYYMMDD format.  # noqa: E501

        :param startdate: The startdate of this DateParametersSummary.  # noqa: E501
        :type: str
        """

        self._startdate = startdate

    @property
    def enddate(self):
        """Gets the enddate of this DateParametersSummary.  # noqa: E501

        End date in YYYYMMDD format.  # noqa: E501

        :return: The enddate of this DateParametersSummary.  # noqa: E501
        :rtype: str
        """
        return self._enddate

    @enddate.setter
    def enddate(self, enddate):
        """Sets the enddate of this DateParametersSummary.

        End date in YYYYMMDD format.  # noqa: E501

        :param enddate: The enddate of this DateParametersSummary.  # noqa: E501
        :type: str
        """

        self._enddate = enddate

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
        if not isinstance(other, DateParametersSummary):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DateParametersSummary):
            return True

        return self.to_dict() != other.to_dict()