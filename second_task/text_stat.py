# Статистика текста
# Необходимо разработать функцию text_stat(filename), которая по заданному имени файла
# рассчитывала статистику его содержимого. Статистика должна рассчитываться для следующих
# категорий:
# • Частота использования каждой буквы латинского или кириллического алфавита
# • Количество слов в тексте
# • Количество абзацев в тексте
# • Доля слов, в которых встречается конкретная буква. Если буква встречается в слове более
# одного раза, считать это одним попаданием буквы в слово
# • Количество слов, в которых одновременно встречаются буквы обоих алфавитов
# Функция должна возвращать словарь со следующим содержимым:
# • Ключ - буква алфавита, значение – tuple (частота_использования_буквы,
# доля_слов_с_буквой)
# • Ключ – word_amount, значение – количество слов в тексте
# • Ключ – paragraph_amount, значение – количество абзацев в тексте
# • Ключ – bilingual_word_amount, значение – количество слов с использованием букв из
# обоих алфавитов
# Функция должна корректно обрабатывать некорректное значение аргумента, возвращая словарь с
# ключом error и значением с кратким описанием проблемы

# ===========================================================================================
# ===========================================================================================
from collections import Counter
from typing import Dict, Union, Tuple


def text_stat(filename: str) -> Dict[str, Union[int, str, Tuple[int]]]:

    if type(filename) is not str:
        return {'error': 'Incorrect argument type'}

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        return {'error': 'File not found.'}
    except:
        return {'error': 'Unknown error occurred.'}

    letters = [char.lower() for char in text if char.isalpha()]
    letter_frequency = dict(Counter(letters))
    words = text.split()
    words_and_letters_amount = {}
    bilingual_word_amount = 0
    russian_alphabet = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    english_alphabet = set('abcdefghijklmnopqrstuvwxyz')

    for word in words:
        english_letter = False
        russian_letter = False
        for letter in word:
            if letter.lower() in english_alphabet:
                english_letter = True
            elif letter.lower() in russian_alphabet:
                russian_letter = True
        if english_letter and russian_letter:
            bilingual_word_amount += 1

    for letter in letter_frequency:
        words_with_letter = [word for word in words if letter.lower() in word.lower()]
        letter_presence_ratio = len(words_with_letter)
        words_and_letters_amount[letter] = (letter_frequency[letter], letter_presence_ratio)

    result = {
        **words_and_letters_amount,
        'paragraph_amount': len(text.split('\n')),
        'word_amount': len(words),
        'bilingual_word_amount': bilingual_word_amount,
    }

    return result
