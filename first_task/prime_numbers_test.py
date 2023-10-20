from unittest import TestCase, main

from first_task.prime_numbers import prime_numbers


class PrimeNumbersTest(TestCase):
    def test_correct_arguments(self):
        self.assertEqual(prime_numbers(1, 10), [2, 3, 5, 7])

    def test_not_a_number_arguments(self):
        self.assertEqual(prime_numbers('hello', 'world'), [])

    def test_incorrect_number_arguments(self):
        self.assertEqual(prime_numbers(7, 3), [])


if __name__ == '__main__':
    main()
