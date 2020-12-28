import unittest
from string_cleaner import StringUtilities


class TestStringCleaner(unittest.TestCase):
    def setUp(self):
        self.string = StringUtilities()

    def tearDown(self):
        self.string = None

    def test_lower_and_strip(self):
        result = self.string.lower_and_strip('  Hello     ')
        self.assertEqual(result, 'hello')

    def test_lower_and_strip_raises_error(self):
        with self.assertRaises(AttributeError):
            result = self.string.lower_and_strip(2)

    def test_reverse_string(self):
        result = self.string.reverse_string('hello')
        self.assertEqual(result, 'olleh')

    def test_reverse_string_raises_error(self):
        with self.assertRaises(TypeError):
            result = self.string.reverse_string(2)


if __name__ == '__main__':
    unittest.main()
