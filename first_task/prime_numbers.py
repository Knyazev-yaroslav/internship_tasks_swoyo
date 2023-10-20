# Простые числа в заданном диапазоне.
# Необходимо разработать функцию prime_numbers(low, high), где low и high – нижняя и верхняя
# границы диапазона, в котором надо найти эти числа. Функция должна возвращать список с
# числами, отсортированными по возрастанию.
# Функция должна корректно обрабатывать некорректное значение аргументов, возвращая пустой
# список

# ===========================================================================================
# ===========================================================================================
from typing import List


def prime_numbers(low: int, high: int) -> List[int]:
    primes = []

    if type(low) is not int or type(high) is not int:
        return primes

    if low > high:
        return primes

    is_prime = [True] * (high + 1)

    if low < 2:
        low = 2

    for num in range(2, int(high ** 0.5) + 1):
        if is_prime[num]:
            for multiple in range(num * num, high + 1, num):
                is_prime[multiple] = False

    primes = [num for num in range(low, high + 1) if is_prime[num]]

    return primes
