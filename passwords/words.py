from os import path
from random import SystemRandom
from itertools import islice


class Selector:
    """Selects random words from a dictionary file"""

    def __init__(self, dict_file):
        if not path.isfile(dict_file):
            raise ValueError("Dictionary file {} is not a valid file".format(dict_file))
        else:
            self._dict_file = dict_file
        self._last_line_num = Selector._file_line_count(self._dict_file)
        self._max_len = self._get_max_word_length()

    def select_word(self, min_len, max_len):
        """Returns a dictionary word, securely selected at random"""
        if max_len > self._max_len:
            max_len = self._max_len
        if not (isinstance(min_len, int) and isinstance(max_len, int)):
            raise TypeError("min_len and max_len must both be positive ints")
        if min_len <= 0:
            raise ValueError("min_len must be a positive int")
        if max_len < min_len:
            raise ValueError("max_len must be greater than min_len")

        while True:
            word = self._read_line(self._random_line_num).strip()
            if word.isalpha() and (min_len <= len(word) <= max_len):
                return word

    def _read_line(self, line_num):
        with open(self._dict_file) as fp:
            for aline in islice(fp, line_num - 1, line_num):
                return aline

    @property
    def _random_line_num(self):
        return SystemRandom().randrange(1, self._last_line_num)

    def _get_max_word_length(self):
        with open(self._dict_file, 'r') as fp:
            return len(max(fp, key=len))

    @staticmethod
    def _file_line_count(file_name):
        with open(file_name) as file:
            return sum(1 for line in file)
