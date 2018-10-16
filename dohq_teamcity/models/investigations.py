# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


# from dohq_teamcity.models.investigation import Investigation  # noqa: F401,E501


class Investigations(TeamCityObject):
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
        'href': 'str',
        'investigation': 'list[Investigation]',
        'next_href': 'str',
        'prev_href': 'str'
    }

    attribute_map = {
        'count': 'count',
        'href': 'href',
        'investigation': 'investigation',
        'next_href': 'nextHref',
        'prev_href': 'prevHref'
    }

    def __init__(self, count=None, href=None, investigation=None, next_href=None, prev_href=None, teamcity=None):  # noqa: E501
        """Investigations - a model defined in Swagger"""  # noqa: E501

        self._count = None
        self._href = None
        self._investigation = None
        self._next_href = None
        self._prev_href = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if href is not None:
            self.href = href
        if investigation is not None:
            self.investigation = investigation
        if next_href is not None:
            self.next_href = next_href
        if prev_href is not None:
            self.prev_href = prev_href
        super(Investigations, self).__init__(teamcity=teamcity)

    @property
    def count(self):
        """Gets the count of this Investigations.  # noqa: E501


        :return: The count of this Investigations.  # noqa: E501
        :rtype: int
        """
        if self._count is None:
            self._read_if_needed()
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this Investigations.


        :param count: The count of this Investigations.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def href(self):
        """Gets the href of this Investigations.  # noqa: E501


        :return: The href of this Investigations.  # noqa: E501
        :rtype: str
        """
        if self._href is None:
            self._read_if_needed()
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this Investigations.


        :param href: The href of this Investigations.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def investigation(self):
        """Gets the investigation of this Investigations.  # noqa: E501


        :return: The investigation of this Investigations.  # noqa: E501
        :rtype: list[Investigation]
        """
        if self._investigation is None:
            self._read_if_needed()
        return self._investigation

    @investigation.setter
    def investigation(self, investigation):
        """Sets the investigation of this Investigations.


        :param investigation: The investigation of this Investigations.  # noqa: E501
        :type: list[Investigation]
        """

        self._investigation = investigation

    @property
    def next_href(self):
        """Gets the next_href of this Investigations.  # noqa: E501


        :return: The next_href of this Investigations.  # noqa: E501
        :rtype: str
        """
        if self._next_href is None:
            self._read_if_needed()
        return self._next_href

    @next_href.setter
    def next_href(self, next_href):
        """Sets the next_href of this Investigations.


        :param next_href: The next_href of this Investigations.  # noqa: E501
        :type: str
        """

        self._next_href = next_href

    @property
    def prev_href(self):
        """Gets the prev_href of this Investigations.  # noqa: E501


        :return: The prev_href of this Investigations.  # noqa: E501
        :rtype: str
        """
        if self._prev_href is None:
            self._read_if_needed()
        return self._prev_href

    @prev_href.setter
    def prev_href(self, prev_href):
        """Sets the prev_href of this Investigations.


        :param prev_href: The prev_href of this Investigations.  # noqa: E501
        :type: str
        """

        self._prev_href = prev_href

