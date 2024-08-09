
class SpeakerResult:
    def __init__(self):
        self.idx: int = 0
        self.transcript: str = ''
        self.confidence: float = 0.0

        self.first_word_start_msec: int = 0
        self.first_word_start_time: str = ''

        self.last_word_end_msec: int = 0
        self.last_word_end_time: str = ''

        self.speaker_tag: int = 0
        self.speaker_name: str = ''
        self.speaker_score: float = 0.0
        self.org_pub_id: str = ''
