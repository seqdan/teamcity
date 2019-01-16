# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


# from dohq_teamcity.models.branch_version import BranchVersion  # noqa: F401,E501


class RepositoryState(TeamCityObject):
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
        'timestamp': 'str',
        'count': 'int',
        'branch': 'list[BranchVersion]'
    }

    attribute_map = {
        'timestamp': 'timestamp',
        'count': 'count',
        'branch': 'branch'
    }

    def __init__(self, timestamp=None, count=None, branch=None, teamcity=None):  # noqa: E501
        """RepositoryState - a model defined in Swagger"""  # noqa: E501

        self._timestamp = None
        self._count = None
        self._branch = None
        self.discriminator = None

        if timestamp is not None:
            self.timestamp = timestamp
        if count is not None:
            self.count = count
        if branch is not None:
            self.branch = branch
        super(RepositoryState, self).__init__(teamcity=teamcity)

    @property
    def timestamp(self):
        """Gets the timestamp of this RepositoryState.  # noqa: E501


        :return: The timestamp of this RepositoryState.  # noqa: E501
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this RepositoryState.


        :param timestamp: The timestamp of this RepositoryState.  # noqa: E501
        :type: str
        """

        self._timestamp = timestamp

    @property
    def count(self):
        """Gets the count of this RepositoryState.  # noqa: E501


        :return: The count of this RepositoryState.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this RepositoryState.


        :param count: The count of this RepositoryState.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def branch(self):
        """Gets the branch of this RepositoryState.  # noqa: E501


        :return: The branch of this RepositoryState.  # noqa: E501
        :rtype: list[BranchVersion]
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        """Sets the branch of this RepositoryState.


        :param branch: The branch of this RepositoryState.  # noqa: E501
        :type: list[BranchVersion]
        """

        self._branch = branch
