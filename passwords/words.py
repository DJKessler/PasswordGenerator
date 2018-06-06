from os import path
from random import SystemRandom
from itertools import islice

_NUM_ROLLS = 5
_DICT_FILENAME = "data/five-dice-wordlist.txt"

class Selector:
    """Selects random words from a dictionary file"""

    def __init__(self):
        if not path.isfile(_DICT_FILENAME):
            raise ValueError("Dictionary file {} is not a valid file".format(dict_file))
        else:
            self._dict_file = _DICT_FILENAME
        self._digest_words()
        self._max_len = self.longest_word_length
        self._min_len = self.shortest_word_length

    def select_word(self, min_len, max_len):
        """Returns a dictionary word, securely selected at random"""
        if not (isinstance(min_len, int) and isinstance(max_len, int)):
            raise TypeError("min_len and max_len must both be positive ints")
        if min_len <= 0:
            raise ValueError("min_len must be a positive int")
        if max_len < min_len:
            raise ValueError("max_len must be greater than min_len")
        if max_len > self._max_len:
            max_len = self._max_len
        if min_len < self._min_len:
            min_len = self._min_len

        while True:
            word = self.random_word()
            if word.isalpha() and (min_len <= len(word) <= max_len):
                return word

    def _digest_words(self):
        self._wordlist = dict()
        with open(self._dict_file) as fp:
            for line in fp:
                parts = line.split()
                self._wordlist[parts[0]] = parts[1]

    @staticmethod
    def _random_key():
        key = ''
        while len(key) < _NUM_ROLLS:
            key += str(SystemRandom().randrange(1, 6))
        return key

    def random_word(self):
        return self._wordlist[Selector._random_key()]

    @property
    def longest_word_length(self):
        return len(max(self._wordlist.values(), key=len))

    @property
    def shortest_word_length(self):
        return len(min(self._wordlist.values(), key=len))
