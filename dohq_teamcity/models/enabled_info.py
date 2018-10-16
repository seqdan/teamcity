# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


# from dohq_teamcity.models.comment import Comment  # noqa: F401,E501


class EnabledInfo(TeamCityObject):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'comment': 'Comment',
        'status': 'bool',
        'status_switch_time': 'str'
    }

    attribute_map = {
        'comment': 'comment',
        'status': 'status',
        'status_switch_time': 'statusSwitchTime'
    }

    def __init__(self, comment=None, status=False, status_switch_time=None, teamcity=None):  # noqa: E501
        """EnabledInfo - a model defined in Swagger"""  # noqa: E501

        self._comment = None
        self._status = None
        self._status_switch_time = None
        self.discriminator = None

        if comment is not None:
            self.comment = comment
        if status is not None:
            self.status = status
        if status_switch_time is not None:
            self.status_switch_time = status_switch_time
        super(EnabledInfo, self).__init__(teamcity=teamcity)

    @property
    def comment(self):
        """Gets the comment of this EnabledInfo.  # noqa: E501


        :return: The comment of this EnabledInfo.  # noqa: E501
        :rtype: Comment
        """
        if self._comment is None:
            self._read_if_needed()
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this EnabledInfo.


        :param comment: The comment of this EnabledInfo.  # noqa: E501
        :type: Comment
        """

        self._comment = comment

    @property
    def status(self):
        """Gets the status of this EnabledInfo.  # noqa: E501


        :return: The status of this EnabledInfo.  # noqa: E501
        :rtype: bool
        """
        if self._status is None:
            self._read_if_needed()
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this EnabledInfo.


        :param status: The status of this EnabledInfo.  # noqa: E501
        :type: bool
        """

        self._status = status

    @property
    def status_switch_time(self):
        """Gets the status_switch_time of this EnabledInfo.  # noqa: E501


        :return: The status_switch_time of this EnabledInfo.  # noqa: E501
        :rtype: str
        """
        if self._status_switch_time is None:
            self._read_if_needed()
        return self._status_switch_time

    @status_switch_time.setter
    def status_switch_time(self, status_switch_time):
        """Sets the status_switch_time of this EnabledInfo.


        :param status_switch_time: The status_switch_time of this EnabledInfo.  # noqa: E501
        :type: str
        """

        self._status_switch_time = status_switch_time

