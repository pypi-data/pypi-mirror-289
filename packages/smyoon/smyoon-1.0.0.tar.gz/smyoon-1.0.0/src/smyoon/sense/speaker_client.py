from typing import List, Optional
from urllib.parse import quote_plus

import requests

from smyoon.sense import config, CochlSenseException
from requests import Response


class SpeakerClient:
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

    @classmethod
    def _result(cls, resp: Response) -> Optional[dict]:
        try:
            resp_json = resp.json()
        except ValueError as err:
            raise err

        if 'error' in resp_json and resp_json['error'] != '':
            raise CochlSenseException(resp_json['error'])

        if 'data' in resp_json:
            return resp_json['data']
        else:
            return None

    def get_all(self) -> Optional[dict]:
        return self._result(requests.get(self.api_config.get_speaker_host() + '/speakers', headers={
            'X-Api-Key': self.project_key,
        }))

    def add(self, speaker: str, file_paths: List[str]) -> Optional[dict]:
        return self._result(requests.post(self.api_config.get_speaker_host() + '/speaker', data={
            'speaker': speaker,
        }, headers={
            'X-Api-Key': self.project_key,
        }, files={
            'file1': open(file_paths[0], 'rb'),
            'file2': open(file_paths[1], 'rb'),
            'file3': open(file_paths[2], 'rb'),
            'file4': open(file_paths[3], 'rb'),
            'file5': open(file_paths[4], 'rb'),
        }))

    def remove(self, speaker: str) -> Optional[dict]:
        return self._result(
            requests.delete(self.api_config.get_speaker_host() + '/speaker?speaker={}'.format(quote_plus(speaker)),
                            headers={'X-Api-Key': self.project_key}))

    def recognize(self, file_path: str) -> Optional[dict]:
        return self._result(requests.post(self.api_config.get_speaker_host() + '/speaker/recognition', headers={
            'X-Api-Key': self.project_key,
        }, files={
            'file': open(file_path, 'rb')
        }))
