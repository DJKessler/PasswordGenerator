"""Secure random password generation"""

from passwords import words

_DICT_FILENAME = '/usr/share/dict/words'
_MIN_WORD_LENGTH = 4
_MIN_NUM_WORDS = 2


class Generator:
    """Generates secure random passwords"""

    def __init__(self, min_len=20, max_len=50,
                 separator='-', min_word_len=_MIN_WORD_LENGTH, dictionary_file=_DICT_FILENAME):
        self._min_num_words = _MIN_NUM_WORDS
        self._file_name = dictionary_file
        self._min_word_len = min_word_len
        self._min_len = min_len
        self._max_len = max_len
        self._separator = separator
        self._words = []
        self._selector = words.Selector(self._file_name)

    def generate(self):
        """Generates a password"""
        self._words = []
        while self._length <= self._min_len or self._num_words < self._min_num_words:
            if self._remaining_length < self._min_word_len:
                break
            self._words.append(self._get_next_word())
        return self._separator.join([segment.title() for segment in self._words])

    @property
    def _length(self):
        return self._length_of_words + self._length_of_separators

    @property
    def _num_words(self):
        return len(self._words)

    @property
    def _length_of_words(self):
        return sum(len(s) for s in self._words)

    @property
    def _length_of_separators(self):
        return (self._num_words - 1) * len(self._separator)

    def _get_next_word(self):
        min_length = self._min_word_len
        max_length = self._remaining_length
        return self._selector.select_word(min_length, max_length)

    @property
    def _remaining_length(self):
        return self._max_len - (self._length + len(self._separator))
