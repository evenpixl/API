import json
from constants import CONSTANTS
import io


class Config(object):
    """Offer configuration helpers."""

    def __init__(self, config_file):
        """
        Parameters
        ----------
        file : str
        The file which will be used as the config.
        """
        super(Config, self).__init__()
        self.file = config_file
        self.config_file = None

    def open(self):
        """Open file for reading and writing.
        Returns
        -------
        file
            The configuration file.
        """
        self.config_file = open(self.file, "r+")
        self.config_file.seek(0)

    def read(self, to_json=True):
        """Reads the given path.
        Parameters
        ----------
        to_json : bool, optional
            Convert into a dictionary if True. Defaults to True.

        Returns
        -------
        str or dict
            Configuration.
        """
        # Open configuration file
        self.open()

        if to_json:
            try:
                content = json.load(self.config_file)
                self.content = content
            except ValueError:
                self.config_file.close()
                self.write(json.dumps(CONSTANTS.DEFAULT_CONFIG))
                self.content = CONSTANTS.DEFAULT_CONFIG
        # Close config file to be able to see manual edits
        self.config_file.close()

        return self.content

    def write(self, content):
        """Write the edited config
        Parameters
        ----------
        content : dict
            The content to write

        Raises
        ------
        TypeError
            If content is not a dict.
        """
        # Open configuration file
        self.open()
        self.config_file.write(content)
