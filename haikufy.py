from typing import *
from syllabipy.sonoripy import SonoriPy
import random

class Haikufy():

    def __init__(self, track_names: List[str]):
        self.track_names = track_names
        self.syl_dict = None
        self.syllabilfy()
        line1 = random.choice(self.create_lines(5))
        line2 = random.choice(self.create_lines(7))
        line3 = random.choice(self.create_lines(5))
        self.haiku = line1 + '\n' + line2 + '\n' + line3

    def syllabilfy(self):
        self.syl_dict = {}

        for count, track_syl in enumerate(map(lambda x: len(SonoriPy(x)), self.track_names)):
            if track_syl == 0:
                continue
            self.syl_dict.update({self.track_names[count]: track_syl})

    def create_lines(self, syllables: int, current_line=''):

        if syllables == 0:
            return [current_line]

        potential_lines = []
        temp_dict = self.syl_dict.copy()
        for count, track_dict in enumerate(temp_dict.items()):
            track_name, track_syllables = track_dict
            if track_syllables <= syllables:
                potential_line = current_line + ' ' + track_name
                potential_syllables_to_find = syllables - track_syllables
                self.syl_dict.pop(track_name)
                potential_lines += self.create_lines(potential_syllables_to_find, current_line=potential_line)
                self.syl_dict.update({track_name: track_syllables})

        return potential_lines
