"""Secure random password generation"""

from random import SystemRandom
from itertools import islice

_DICT_FILENAME = '/usr/share/dict/words'
_MIN_WORD_LENGTH = 4
_MIN_NUM_WORDS = 2


class RandomWordSelector:
    """Securely selects random words from a dictonary file"""

    def __init__(self, dict_file=_DICT_FILENAME):
        self._dict_file = dict_file
        self._file_length = sum(1 for line in open(dict_file))

    def select_word(self, min_len, max_len):
        """Returns a dictionary word, securely selected at random"""
        if max_len < min_len:
            raise ValueError

        while True:
            line_num = SystemRandom().randrange(1, self._file_length)
            word = self._get_line(line_num).strip()
            if word.isalpha() and (min_len <= len(word) <= max_len):
                break
        return word

    def _get_line(self, line_number):
        with open(self._dict_file) as file_ptr:
            for aline in islice(file_ptr, line_number - 1, line_number):
                return aline


class Password:
    """Generates secure random passwords"""

    def __init__(self, min_total_len=20, max_total_len=50,
                 separator='-', min_word_len=_MIN_WORD_LENGTH, dictionary_file=_DICT_FILENAME):
        self._min_num_segments = _MIN_NUM_WORDS
        self._file_name = dictionary_file
        self._min_segment_len = min_word_len
        self._min_total_len = min_total_len
        self._max_total_len = max_total_len
        self._separator = separator

    def __str__(self):
        return self.generate()

    def generate(self):
        """Generates a password"""
        length = 0
        segments_length = 0
        segments = []
        while length <= self._min_total_len or len(segments) < self._min_num_segments:
            segments.append(self._get_next_segment(segments))
            segments_length += len(segments[-1])
            length = segments_length + (len(self._separator) * len(segments) - 1)
        return self._separator.join([segment.title() for segment in segments])

    def _get_next_segment(self, segments):
        min_length = self._min_segment_len
        max_length = self._remaining_length(segments)
        return RandomWordSelector(self._file_name).select_word(min_length, max_length)

    def _remaining_length(self, segments):
        length_of_separators = self._get_length_of_separators(segments)
        length_of_segments = sum(len(s) for s in segments)
        return self._max_total_len - (length_of_segments + length_of_separators)

    def _get_length_of_separators(self, segments):
        return (len(segments) - 1) * len(self._separator) if len(segments) > 0 else 0
