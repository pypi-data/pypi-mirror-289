from typing import Optional

from smyoon.sense._event_result import _EventResult
from smyoon.sense.speaker_result import SpeakerResult


class FileResult:
    def __init__(self):
        self.events: Optional[_EventResult] = None
        self.speakers: Optional[SpeakerResult] = None
