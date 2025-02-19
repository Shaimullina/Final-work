"""Задача 3: Комплексные числа
Напишите функцию, которая принимает список комплексных чисел
 и возвращает сумму модулей этих чисел.
"""


def sum_of_moduli(complex_numbers: list) -> float:
    list_new = []
    for number in complex_numbers:
        list_new.append(abs(number))
    sum_of_moduli_final = sum(list_new)
    return sum_of_moduli_final


complex_numbers = [complex(3, 4), complex(1, 1), complex(0, 2)]
print(sum_of_moduli(complex_numbers))
