from unittest import TestCase

from util.string_utils import to_padded_string


class TestStringUtils(TestCase):

    def test_to_padded_string_none_number(self):
        self.assertEqual('___', to_padded_string(None, '_', 3))

    def test_to_padded_string_empty_number(self):
        self.assertEqual('____', to_padded_string('', '_', 4))
        
    def test_to_padded_string_no_digits(self):
        self.assertEqual('1234', to_padded_string(1234))

    def test_to_padded_string_less_digits(self):
        self.assertEqual('34', to_padded_string(1234, digits=2))

    def test_to_padded_string_more_digits(self):
        self.assertEqual('001234', to_padded_string(1234, digits=6))

    def test_to_padded_string_exact_digits(self):
        self.assertEqual('1234', to_padded_string(1234, digits=4))

    def test_to_padded_string_custom_padding_value(self):
        self.assertEqual('__1234', to_padded_string(1234, digits=6, padding_value='_'))

