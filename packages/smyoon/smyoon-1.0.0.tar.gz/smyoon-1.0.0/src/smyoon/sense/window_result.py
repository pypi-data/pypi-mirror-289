from typing import List


class SoundTag:
    def __init__(self, name: str, probability: float):
        self.name: str = name
        self.probability: float = probability

    def __str__(self):
        return str(vars(self))

    def to_dict(self) -> dict:
        return vars(self).copy()


class WindowResult:
    def __init__(self, start_time: float, end_time: float, sound_tags: List[SoundTag]):
        self.start_time: float = start_time
        self.end_time: float = end_time
        self.sound_tags: List[SoundTag] = sound_tags

    def __str__(self):
        v: dict = vars(self).copy()
        v['sound_tags'] = [vars(t) for t in v['sound_tags']]
        return str(v)

    def to_dict(self) -> dict:
        v: dict = vars(self).copy()
        v['sound_tags'] = [st.to_dict() for st in self.sound_tags]
        return v
