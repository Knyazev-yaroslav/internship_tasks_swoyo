# Перевод числа, состоящего из римских цифр, в целое число
# Необходимо разработать функцию roman_numerals_to_int(roman_numeral), которая выполнит
# перевод числа из римской нотации в десятичную целочисленную нотацию. Римское число
# задается в виде строки, возвращаемый результат должен иметь тип int, если трансляция прошла
# успешно, либо None, если возникли проблемы с переводом числа.

# ===========================================================================================
# ===========================================================================================
from typing import Union


def roman_numerals_to_int(roman_numeral: str) -> Union[int, None]:
    roman_map = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    result = 0
    i = 0

    if type(roman_numeral) is not str:
        return None

    roman_numbers_list = list(roman_numeral)

    while i < len(roman_numbers_list):

        if roman_map.get(roman_numeral[i]) is None:
            return None

        if i + 1 < len(roman_numbers_list) and roman_map[roman_numbers_list[i]] < roman_map[roman_numbers_list[i + 1]]:
            result += roman_map[roman_numbers_list[i + 1]] - roman_map[roman_numbers_list[i]]
            i += 2
        else:
            result += roman_map[roman_numbers_list[i]]
            i += 1

    return result
