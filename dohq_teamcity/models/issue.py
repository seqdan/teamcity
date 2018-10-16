# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject



class Issue(TeamCityObject):
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
        'id': 'str',
        'url': 'str'
    }

    attribute_map = {
        'id': 'id',
        'url': 'url'
    }

    def __init__(self, id=None, url=None, teamcity=None):  # noqa: E501
        """Issue - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._url = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if url is not None:
            self.url = url
        super(Issue, self).__init__(teamcity=teamcity)

    @property
    def id(self):
        """Gets the id of this Issue.  # noqa: E501


        :return: The id of this Issue.  # noqa: E501
        :rtype: str
        """
        if self._id is None:
            self._read_if_needed()
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Issue.


        :param id: The id of this Issue.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def url(self):
        """Gets the url of this Issue.  # noqa: E501


        :return: The url of this Issue.  # noqa: E501
        :rtype: str
        """
        if self._url is None:
            self._read_if_needed()
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Issue.


        :param url: The url of this Issue.  # noqa: E501
        :type: str
        """

        self._url = url

