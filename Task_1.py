"""Задача 1: Проверка матрицы на симметричность
Напишите функцию, которая принимает на вход квадратную матрицу и проверяет, 
является ли она симметричной относительно главной диагонали."""


def is_symmetric(matrix: list) -> bool:
    flag = True
    for i in range(matrix):
        for j in range(matrix):
            if matrix[i][j] != matrix[j][i] and i != j:
                flag = False
                break
            if flag:
                return flag


matrix = [[1, 2, 3], [2, 4, 5], [3, 5, 6]]
print(is_symmetric(matrix))
