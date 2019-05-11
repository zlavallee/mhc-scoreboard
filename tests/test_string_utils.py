from unittest import TestCase

from string_utils import to_string


class TestStringUtils(TestCase):
    def test_to_string_no_digits(self):
        self.assertEqual('1234', to_string(1234))

    def test_to_string_less_digits(self):
        self.assertEqual('34', to_string(1234, digits=2))

    def test_to_string_more_digits(self):
        self.assertEqual('001234', to_string(1234, digits=6))

    def test_to_string_exact_digits(self):
        self.assertEqual('1234', to_string(1234, digits=4))

    def test_to_string_custom_padding_value(self):
        self.assertEqual('__1234', to_string(1234, digits=6, padding_value='_'))

