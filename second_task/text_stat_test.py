from unittest import TestCase, main

from second_task.text_stat import text_stat


class TextStatTest(TestCase):
    def test_correct_arguments(self):
        expected = {'l': (36, 33), 'o': (28, 24), 'r': (42, 38), 'e': (92, 73), 'm': (31, 26), 'i': (72, 58),
                    'p': (19, 19), 's': (54, 46), 'u': (52, 47), 'd': (25, 25), 't': (42, 39), 'a': (45, 36),
                    'c': (32, 31), 'n': (43, 38), 'g': (5, 5), 'x': (2, 2), 'f': (8, 7), 'h': (6, 6), 'v': (6, 6),
                    'b': (7, 7), 'q': (8, 6), 'к': (26, 24), 'л': (26, 26), 'и': (39, 34), 'е': (53, 47), 'н': (54, 49),
                    'т': (37, 35), 'о': (64, 51), 'ч': (6, 6), 'ь': (11, 11), 'в': (21, 20), 'а': (47, 38),
                    'ж': (15, 15), 'з': (6, 6), 'k': (1, 1), 'м': (18, 15), 'п': (14, 14), 'й': (12, 12), 'д': (28, 27),
                    'с': (22, 21), 'х': (6, 6), 'э': (9, 9), 'ы': (10, 10), 'у': (18, 17), 'р': (18, 18), 'б': (14, 14),
                    'я': (9, 9), 'ш': (4, 4), 'ф': (3, 3), 'г': (8, 6), 'ц': (1, 1), 'ю': (2, 2), 'щ': (1, 1),
                    'paragraph_amount': 4, 'word_amount': 251, 'bilingual_word_amount': 4}
        self.assertEqual(text_stat('test.txt'), expected)

    def test_file_not_found(self):
        expected_error = {'error': 'File not found.'}
        self.assertEqual(text_stat('not_found.txt'), expected_error)

    def test_incorrect_argument_type(self):
        expected_error = {'error': 'Incorrect argument type'}
        self.assertEqual(text_stat(123), expected_error)


if __name__ == '__main__':
    main()
