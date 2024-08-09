import os

from . import config, check_latest_lib_version
from ._event_client import _EventClient
from .file_result import FileResult
from .speaker_client import SpeakerClient


class FileClient:
    """FileClient is used to predict an audio file with Cochl.Sense."""

    def __init__(
        self,
        api_project_key: str,
        api_config: config.APIConfig = None,
    ):
        if not api_project_key:
            raise ValueError(f'invalid project key "{api_project_key}"')
        if api_config is None:
            api_config = config.APIConfig()  # use default APIConfig

        self.project_key: str = api_project_key
        self.api_config: config.APIConfig = api_config

        # check client library version
        check_latest_lib_version(self.api_config.get_event_host())

    def predict(self, file_path: str) -> FileResult:
        """
        Predicts the given file.

        Args:
            file_path: Path to the file. For example, '/Users/user/file.mp3'
        """

        if not os.path.exists(file_path):
            raise FileNotFoundError(file_path)

        file_result = FileResult()

        event_file_client = _EventClient(self.project_key, self.api_config)
        file_result.events = event_file_client.predict(file_path)

        if not self.api_config.speaker_recognition:
            return file_result

        if '[Speech]' not in file_result.events.to_summarized_result():
            return file_result

        speaker_file_client = SpeakerClient(self.project_key, self.api_config)
        file_result.speakers = speaker_file_client.recognize(file_path)

        return file_result
