from unittest import TestCase, main

from third_task.roman_numerals_to_int import roman_numerals_to_int


class RomanNumeralToIntTest(TestCase):
    def test_correct_arguments(self):
        self.assertEqual(roman_numerals_to_int("XVIII"), 18)

    def test_argument_is_not_roman_numeral(self):
        self.assertEqual(roman_numerals_to_int("ASD"), None)

    def test_is_not_string_argument(self):
        self.assertEqual(roman_numerals_to_int(123), None)


if __name__ == '__main__':
    main()
