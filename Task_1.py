"""Задача 1: Проверка матрицы на симметричность
Напишите функцию, которая принимает на вход квадратную матрицу и проверяет, 
является ли она симметричной относительно главной диагонали."""


def is_symmetric(matrix: list) -> bool:
    n = int(input())
    matrix = []
    flag = True
    for _ in range(n):
        matrix_n = [int(x) for x in input().split()]
        matrix.append(matrix_n)

    for i in range(n):
        for j in range(n):
            if matrix[i][q] != matrix[j][i] and i != j:
                flag = False
                break
        if flag:
            return matrix


print(is_symmetric(matrix))  # True
