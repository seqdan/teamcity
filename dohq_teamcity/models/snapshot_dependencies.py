# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


# from dohq_teamcity.models.snapshot_dependency import SnapshotDependency  # noqa: F401,E501


class SnapshotDependencies(TeamCityObject):
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
        'count': 'int',
        'snapshot_dependency': 'list[SnapshotDependency]'
    }

    attribute_map = {
        'count': 'count',
        'snapshot_dependency': 'snapshot-dependency'
    }

    def __init__(self, count=None, snapshot_dependency=None, teamcity=None):  # noqa: E501
        """SnapshotDependencies - a model defined in Swagger"""  # noqa: E501

        self._count = None
        self._snapshot_dependency = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if snapshot_dependency is not None:
            self.snapshot_dependency = snapshot_dependency
        super(SnapshotDependencies, self).__init__(teamcity=teamcity)

    @property
    def count(self):
        """Gets the count of this SnapshotDependencies.  # noqa: E501


        :return: The count of this SnapshotDependencies.  # noqa: E501
        :rtype: int
        """
        if self._count is None:
            self._read_if_needed()
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this SnapshotDependencies.


        :param count: The count of this SnapshotDependencies.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def snapshot_dependency(self):
        """Gets the snapshot_dependency of this SnapshotDependencies.  # noqa: E501


        :return: The snapshot_dependency of this SnapshotDependencies.  # noqa: E501
        :rtype: list[SnapshotDependency]
        """
        if self._snapshot_dependency is None:
            self._read_if_needed()
        return self._snapshot_dependency

    @snapshot_dependency.setter
    def snapshot_dependency(self, snapshot_dependency):
        """Sets the snapshot_dependency of this SnapshotDependencies.


        :param snapshot_dependency: The snapshot_dependency of this SnapshotDependencies.  # noqa: E501
        :type: list[SnapshotDependency]
        """

        self._snapshot_dependency = snapshot_dependency

