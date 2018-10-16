# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


# from dohq_teamcity.models.file import file  # noqa: F401,E501


class Files(TeamCityObject):
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
        'file': 'list[file]',
        'href': 'str'
    }

    attribute_map = {
        'count': 'count',
        'file': 'file',
        'href': 'href'
    }

    def __init__(self, count=None, file=None, href=None, teamcity=None):  # noqa: E501
        """Files - a model defined in Swagger"""  # noqa: E501

        self._count = None
        self._file = None
        self._href = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if file is not None:
            self.file = file
        if href is not None:
            self.href = href
        super(Files, self).__init__(teamcity=teamcity)

    @property
    def count(self):
        """Gets the count of this Files.  # noqa: E501


        :return: The count of this Files.  # noqa: E501
        :rtype: int
        """
        if self._count is None:
            self._read_if_needed()
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this Files.


        :param count: The count of this Files.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def file(self):
        """Gets the file of this Files.  # noqa: E501


        :return: The file of this Files.  # noqa: E501
        :rtype: list[file]
        """
        if self._file is None:
            self._read_if_needed()
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this Files.


        :param file: The file of this Files.  # noqa: E501
        :type: list[file]
        """

        self._file = file

    @property
    def href(self):
        """Gets the href of this Files.  # noqa: E501


        :return: The href of this Files.  # noqa: E501
        :rtype: str
        """
        if self._href is None:
            self._read_if_needed()
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this Files.


        :param href: The href of this Files.  # noqa: E501
        :type: str
        """

        self._href = href

