"""Secure random password generation"""

from passwords import words

_MIN_WORD_LENGTH = 4
_MIN_NUM_WORDS = 2


class Generator:
    """Generates secure random passwords"""

    def __init__(self, min_len=20, max_len=50, separator='-',
                 min_word_len=_MIN_WORD_LENGTH, maximize_len=True):
        self._min_num_words = _MIN_NUM_WORDS
        self._min_word_len = min_word_len
        self._min_len = min_len
        self._max_len = max_len
        self._separator = separator
        self._words = []
        self._maximize_len = maximize_len
        self._selector = words.Selector()

    def generate(self):
        """Generates a password"""
        self._words = []
        while self._needs_another_word():
            self._words.append(self._next_word)
        if self._length > self._max_len:
            raise OverflowError("Generated password is too long")
        return self.generated_password

    def _needs_another_word(self):
        if self._is_too_short() or self._too_few_words():
            return True
        if self._maximize_len:
            return self._can_fit_another_word()
        return False

    def _can_fit_another_word(self):
        return self._min_word_len < self._remaining_length and self._length < self._max_len

    def _is_too_short(self):
        return self._length < self._min_len

    def _too_few_words(self):
        return self._num_words < self._min_num_words

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

    @property
    def _next_word(self):
        min_length = self._min_word_len
        max_length = self._remaining_length
        return self._selector.select_word(min_length, max_length)

    @property
    def _remaining_length(self):
        return self._max_len - (self._length + len(self._separator))

    @property
    def generated_password(self):
        return self._separator.join([word.title() for word in self._words])
