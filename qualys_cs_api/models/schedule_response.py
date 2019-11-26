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


class ScheduleResponse(object):
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
        'created': 'str',
        'errors': 'list[CMSError]',
        'filters': 'list[Filter]',
        'job_completion_date': 'str',
        'job_listing_completion_date': 'str',
        'job_listing_start_date': 'str',
        'job_scanning_completion_date': 'str',
        'job_scanning_start_date': 'str',
        'job_start_date': 'str',
        'name': 'str',
        'on_demand': 'bool',
        'schedule': 'str',
        'schedule_uuid': 'str',
        'status': 'str',
        'updated': 'str'
    }

    attribute_map = {
        'created': 'created',
        'errors': 'errors',
        'filters': 'filters',
        'job_completion_date': 'jobCompletionDate',
        'job_listing_completion_date': 'jobListingCompletionDate',
        'job_listing_start_date': 'jobListingStartDate',
        'job_scanning_completion_date': 'jobScanningCompletionDate',
        'job_scanning_start_date': 'jobScanningStartDate',
        'job_start_date': 'jobStartDate',
        'name': 'name',
        'on_demand': 'onDemand',
        'schedule': 'schedule',
        'schedule_uuid': 'scheduleUuid',
        'status': 'status',
        'updated': 'updated'
    }

    def __init__(self, created=None, errors=None, filters=None, job_completion_date=None, job_listing_completion_date=None, job_listing_start_date=None, job_scanning_completion_date=None, job_scanning_start_date=None, job_start_date=None, name=None, on_demand=None, schedule=None, schedule_uuid=None, status=None, updated=None, local_vars_configuration=None):  # noqa: E501
        """ScheduleResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._created = None
        self._errors = None
        self._filters = None
        self._job_completion_date = None
        self._job_listing_completion_date = None
        self._job_listing_start_date = None
        self._job_scanning_completion_date = None
        self._job_scanning_start_date = None
        self._job_start_date = None
        self._name = None
        self._on_demand = None
        self._schedule = None
        self._schedule_uuid = None
        self._status = None
        self._updated = None
        self.discriminator = None

        if created is not None:
            self.created = created
        if errors is not None:
            self.errors = errors
        if filters is not None:
            self.filters = filters
        if job_completion_date is not None:
            self.job_completion_date = job_completion_date
        if job_listing_completion_date is not None:
            self.job_listing_completion_date = job_listing_completion_date
        if job_listing_start_date is not None:
            self.job_listing_start_date = job_listing_start_date
        if job_scanning_completion_date is not None:
            self.job_scanning_completion_date = job_scanning_completion_date
        if job_scanning_start_date is not None:
            self.job_scanning_start_date = job_scanning_start_date
        if job_start_date is not None:
            self.job_start_date = job_start_date
        if name is not None:
            self.name = name
        if on_demand is not None:
            self.on_demand = on_demand
        if schedule is not None:
            self.schedule = schedule
        if schedule_uuid is not None:
            self.schedule_uuid = schedule_uuid
        if status is not None:
            self.status = status
        if updated is not None:
            self.updated = updated

    @property
    def created(self):
        """Gets the created of this ScheduleResponse.  # noqa: E501


        :return: The created of this ScheduleResponse.  # noqa: E501
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ScheduleResponse.


        :param created: The created of this ScheduleResponse.  # noqa: E501
        :type: str
        """

        self._created = created

    @property
    def errors(self):
        """Gets the errors of this ScheduleResponse.  # noqa: E501


        :return: The errors of this ScheduleResponse.  # noqa: E501
        :rtype: list[CMSError]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this ScheduleResponse.


        :param errors: The errors of this ScheduleResponse.  # noqa: E501
        :type: list[CMSError]
        """

        self._errors = errors

    @property
    def filters(self):
        """Gets the filters of this ScheduleResponse.  # noqa: E501


        :return: The filters of this ScheduleResponse.  # noqa: E501
        :rtype: list[Filter]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this ScheduleResponse.


        :param filters: The filters of this ScheduleResponse.  # noqa: E501
        :type: list[Filter]
        """

        self._filters = filters

    @property
    def job_completion_date(self):
        """Gets the job_completion_date of this ScheduleResponse.  # noqa: E501


        :return: The job_completion_date of this ScheduleResponse.  # noqa: E501
        :rtype: str
        """
        return self._job_completion_date

    @job_completion_date.setter
    def job_completion_date(self, job_completion_date):
        """Sets the job_completion_date of this ScheduleResponse.


        :param job_completion_date: The job_completion_date of this ScheduleResponse.  # noqa: E501
        :type: str
        """

        self._job_completion_date = job_completion_date

    @property
    def job_listing_completion_date(self):
        """Gets the job_listing_completion_date of this ScheduleResponse.  # noqa: E501


        :return: The job_listing_completion_date of this ScheduleResponse.  # noqa: E501
        :rtype: str
        """
        return self._job_listing_completion_date

    @job_listing_completion_date.setter
    def job_listing_completion_date(self, job_listing_completion_date):
        """Sets the job_listing_completion_date of this ScheduleResponse.


        :param job_listing_completion_date: The job_listing_completion_date of this ScheduleResponse.  # noqa: E501
        :type: str
        """

        self._job_listing_completion_date = job_listing_completion_date

    @property
    def job_listing_start_date(self):
        """Gets the job_listing_start_date of this ScheduleResponse.  # noqa: E501


        :return: The job_listing_start_date of this ScheduleResponse.  # noqa: E501
        :rtype: str
        """
        return self._job_listing_start_date

    @job_listing_start_date.setter
    def job_listing_start_date(self, job_listing_start_date):
        """Sets the job_listing_start_date of this ScheduleResponse.


        :param job_listing_start_date: The job_listing_start_date of this ScheduleResponse.  # noqa: E501
        :type: str
        """

        self._job_listing_start_date = job_listing_start_date

    @property
    def job_scanning_completion_date(self):
        """Gets the job_scanning_completion_date of this ScheduleResponse.  # noqa: E501


        :return: The job_scanning_completion_date of this ScheduleResponse.  # noqa: E501
        :rtype: str
        """
        return self._job_scanning_completion_date

    @job_scanning_completion_date.setter
    def job_scanning_completion_date(self, job_scanning_completion_date):
        """Sets the job_scanning_completion_date of this ScheduleResponse.


        :param job_scanning_completion_date: The job_scanning_completion_date of this ScheduleResponse.  # noqa: E501
        :type: str
        """

        self._job_scanning_completion_date = job_scanning_completion_date

    @property
    def job_scanning_start_date(self):
        """Gets the job_scanning_start_date of this ScheduleResponse.  # noqa: E501


        :return: The job_scanning_start_date of this ScheduleResponse.  # noqa: E501
        :rtype: str
        """
        return self._job_scanning_start_date

    @job_scanning_start_date.setter
    def job_scanning_start_date(self, job_scanning_start_date):
        """Sets the job_scanning_start_date of this ScheduleResponse.


        :param job_scanning_start_date: The job_scanning_start_date of this ScheduleResponse.  # noqa: E501
        :type: str
        """

        self._job_scanning_start_date = job_scanning_start_date

    @property
    def job_start_date(self):
        """Gets the job_start_date of this ScheduleResponse.  # noqa: E501


        :return: The job_start_date of this ScheduleResponse.  # noqa: E501
        :rtype: str
        """
        return self._job_start_date

    @job_start_date.setter
    def job_start_date(self, job_start_date):
        """Sets the job_start_date of this ScheduleResponse.


        :param job_start_date: The job_start_date of this ScheduleResponse.  # noqa: E501
        :type: str
        """

        self._job_start_date = job_start_date

    @property
    def name(self):
        """Gets the name of this ScheduleResponse.  # noqa: E501


        :return: The name of this ScheduleResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ScheduleResponse.


        :param name: The name of this ScheduleResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def on_demand(self):
        """Gets the on_demand of this ScheduleResponse.  # noqa: E501


        :return: The on_demand of this ScheduleResponse.  # noqa: E501
        :rtype: bool
        """
        return self._on_demand

    @on_demand.setter
    def on_demand(self, on_demand):
        """Sets the on_demand of this ScheduleResponse.


        :param on_demand: The on_demand of this ScheduleResponse.  # noqa: E501
        :type: bool
        """

        self._on_demand = on_demand

    @property
    def schedule(self):
        """Gets the schedule of this ScheduleResponse.  # noqa: E501


        :return: The schedule of this ScheduleResponse.  # noqa: E501
        :rtype: str
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this ScheduleResponse.


        :param schedule: The schedule of this ScheduleResponse.  # noqa: E501
        :type: str
        """

        self._schedule = schedule

    @property
    def schedule_uuid(self):
        """Gets the schedule_uuid of this ScheduleResponse.  # noqa: E501


        :return: The schedule_uuid of this ScheduleResponse.  # noqa: E501
        :rtype: str
        """
        return self._schedule_uuid

    @schedule_uuid.setter
    def schedule_uuid(self, schedule_uuid):
        """Sets the schedule_uuid of this ScheduleResponse.


        :param schedule_uuid: The schedule_uuid of this ScheduleResponse.  # noqa: E501
        :type: str
        """

        self._schedule_uuid = schedule_uuid

    @property
    def status(self):
        """Gets the status of this ScheduleResponse.  # noqa: E501


        :return: The status of this ScheduleResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ScheduleResponse.


        :param status: The status of this ScheduleResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["Created", "Queued", "Paused", "Running", "Completed", "Finished", "Error", "Failed", "BaselineCompleted", "BaselineCreated", "BaselineQueued", "BaselineRunning", "Canceled"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def updated(self):
        """Gets the updated of this ScheduleResponse.  # noqa: E501


        :return: The updated of this ScheduleResponse.  # noqa: E501
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this ScheduleResponse.


        :param updated: The updated of this ScheduleResponse.  # noqa: E501
        :type: str
        """

        self._updated = updated

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
        if not isinstance(other, ScheduleResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ScheduleResponse):
            return True

        return self.to_dict() != other.to_dict()
