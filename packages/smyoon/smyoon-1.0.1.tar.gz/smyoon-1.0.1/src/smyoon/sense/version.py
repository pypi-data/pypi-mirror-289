import requests
import warnings

from requests import RequestException, Response

from . import __version__


def check_latest_lib_version(host: str) -> None:
    url: str = f'{host}/client-libraries/latest'
    params: dict = {'current_version': __version__}

    try:
        response: Response = requests.get(url, params=params)
        if response.status_code == 200:
            latest_version: str = response.json().get('version')

            if __version__ != latest_version:
                warnings.warn(
                    f'Warning! The library version is outdated. '
                    f'Please upgrade the library: pip3 install cochl=={latest_version}',
                    stacklevel=3
                )
        else:
            pass
    except RequestException as _e:
        pass
