# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject



class FileChange(TeamCityObject):
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
        'after_revision': 'str',
        'before_revision': 'str',
        'change_type': 'str',
        'change_type_comment': 'str',
        'directory': 'bool',
        'file': 'str',
        'relative_file': 'str'
    }

    attribute_map = {
        'after_revision': 'after-revision',
        'before_revision': 'before-revision',
        'change_type': 'changeType',
        'change_type_comment': 'changeTypeComment',
        'directory': 'directory',
        'file': 'file',
        'relative_file': 'relative-file'
    }

    def __init__(self, after_revision=None, before_revision=None, change_type=None, change_type_comment=None, directory=False, file=None, relative_file=None, teamcity=None):  # noqa: E501
        """FileChange - a model defined in Swagger"""  # noqa: E501

        self._after_revision = None
        self._before_revision = None
        self._change_type = None
        self._change_type_comment = None
        self._directory = None
        self._file = None
        self._relative_file = None
        self.discriminator = None

        if after_revision is not None:
            self.after_revision = after_revision
        if before_revision is not None:
            self.before_revision = before_revision
        if change_type is not None:
            self.change_type = change_type
        if change_type_comment is not None:
            self.change_type_comment = change_type_comment
        if directory is not None:
            self.directory = directory
        if file is not None:
            self.file = file
        if relative_file is not None:
            self.relative_file = relative_file
        super(FileChange, self).__init__(teamcity=teamcity)

    @property
    def after_revision(self):
        """Gets the after_revision of this FileChange.  # noqa: E501


        :return: The after_revision of this FileChange.  # noqa: E501
        :rtype: str
        """
        if self._after_revision is None:
            self._read_if_needed()
        return self._after_revision

    @after_revision.setter
    def after_revision(self, after_revision):
        """Sets the after_revision of this FileChange.


        :param after_revision: The after_revision of this FileChange.  # noqa: E501
        :type: str
        """

        self._after_revision = after_revision

    @property
    def before_revision(self):
        """Gets the before_revision of this FileChange.  # noqa: E501


        :return: The before_revision of this FileChange.  # noqa: E501
        :rtype: str
        """
        if self._before_revision is None:
            self._read_if_needed()
        return self._before_revision

    @before_revision.setter
    def before_revision(self, before_revision):
        """Sets the before_revision of this FileChange.


        :param before_revision: The before_revision of this FileChange.  # noqa: E501
        :type: str
        """

        self._before_revision = before_revision

    @property
    def change_type(self):
        """Gets the change_type of this FileChange.  # noqa: E501


        :return: The change_type of this FileChange.  # noqa: E501
        :rtype: str
        """
        if self._change_type is None:
            self._read_if_needed()
        return self._change_type

    @change_type.setter
    def change_type(self, change_type):
        """Sets the change_type of this FileChange.


        :param change_type: The change_type of this FileChange.  # noqa: E501
        :type: str
        """

        self._change_type = change_type

    @property
    def change_type_comment(self):
        """Gets the change_type_comment of this FileChange.  # noqa: E501


        :return: The change_type_comment of this FileChange.  # noqa: E501
        :rtype: str
        """
        if self._change_type_comment is None:
            self._read_if_needed()
        return self._change_type_comment

    @change_type_comment.setter
    def change_type_comment(self, change_type_comment):
        """Sets the change_type_comment of this FileChange.


        :param change_type_comment: The change_type_comment of this FileChange.  # noqa: E501
        :type: str
        """

        self._change_type_comment = change_type_comment

    @property
    def directory(self):
        """Gets the directory of this FileChange.  # noqa: E501


        :return: The directory of this FileChange.  # noqa: E501
        :rtype: bool
        """
        if self._directory is None:
            self._read_if_needed()
        return self._directory

    @directory.setter
    def directory(self, directory):
        """Sets the directory of this FileChange.


        :param directory: The directory of this FileChange.  # noqa: E501
        :type: bool
        """

        self._directory = directory

    @property
    def file(self):
        """Gets the file of this FileChange.  # noqa: E501


        :return: The file of this FileChange.  # noqa: E501
        :rtype: str
        """
        if self._file is None:
            self._read_if_needed()
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this FileChange.


        :param file: The file of this FileChange.  # noqa: E501
        :type: str
        """

        self._file = file

    @property
    def relative_file(self):
        """Gets the relative_file of this FileChange.  # noqa: E501


        :return: The relative_file of this FileChange.  # noqa: E501
        :rtype: str
        """
        if self._relative_file is None:
            self._read_if_needed()
        return self._relative_file

    @relative_file.setter
    def relative_file(self, relative_file):
        """Sets the relative_file of this FileChange.


        :param relative_file: The relative_file of this FileChange.  # noqa: E501
        :type: str
        """

        self._relative_file = relative_file

