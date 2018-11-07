import unittest

from passwords import words

class TestSelector(unittest.TestCase):
    def test_constructor(self):
        try:
            words.Selector()
        except ExceptionType:
            self.fail("Selector() raised ExceptionType unexpectedly!")

    def test_digest_words(self):
        selector = words.Selector()
        selector._digest_words()

    def test_random_word(self):
        selector = words.Selector()
        try:
            word = selector.random_word()
        except ExceptionType:
            self.fail("Selector.random_word() raised ExceptionType unexpectedly!")

    def test_select_word(self):
        selector = words.Selector()
        min_len = 2
        max_len = 2000
        try:
            word = selector.select_word(min_len, max_len)
        except ExceptionType:
            self.fail("Selector.select_word({}, {}) raised ExceptionType unexpectedly!".format(min_len, max_len))

        min_len = 2.1
        max_len = 3
        self.assertFalse(isinstance(min_len, int) and isinstance(max_len, int))
        with self.assertRaises(TypeError):
            selector.select_word(min_len, max_len)

        min_len = 2
        max_len = 3.1
        self.assertFalse(isinstance(min_len, int) and isinstance(max_len, int))
        with self.assertRaises(TypeError):
            selector.select_word(min_len, max_len)

        min_len = 2.1
        max_len = 3.1
        self.assertFalse(isinstance(min_len, int) and isinstance(max_len, int))
        with self.assertRaises(TypeError):
            selector.select_word(min_len, max_len)

        min_len = -1
        max_len = 3
        self.assertTrue(min_len <= 0)
        with self.assertRaises(ValueError):
            selector.select_word(min_len, max_len)

        min_len = 2
        max_len = 1
        self.assertTrue(max_len < min_len)
        with self.assertRaises(ValueError):
            selector.select_word(min_len, max_len)






if __name__ == '__main__':
    unittest.main()
