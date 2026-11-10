"""Лабораторная 08: создание массивов, индексация и срезы NumPy."""

import numpy as np


# Задание 1. Создание векторов и матриц.
hours = np.arange(0, 24, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2, 3), -1)
identity = np.eye(3)

print("Задание 1")
print("hours:", hours)
print("line:", line)
print("zeros:", zeros)
print("unknown_table:\n", unknown_table)
print("identity:\n", identity)
print("shape:", hours.shape)
print("ndim:", hours.ndim)
print("size:", hours.size)
print("dtype:", hours.dtype)

# Задание 2. Правая граница среза не включается.
print("\nЗадание 2")
print("Третий элемент:", hours[2])
print("Последний элемент:", hours[-1])
print("Индексы 2–5:", hours[2:6])
print("Каждый второй элемент:", hours[::2])
print("Обратный порядок:", hours[::-1])

# Задание 3. Сначала указываются строки, затем столбцы.
temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])
print("\nЗадание 3")
print("Форма:", temperatures.shape)
print("Число измерений:", temperatures.ndim)
print("Число элементов:", temperatures.size)
print("Вторая строка, третий столбец:", temperatures[1, 2])
print("Первая строка:", temperatures[0, :])
print("Последний столбец:", temperatures[:, -1])
print("Первые две строки без первого столбца:\n", temperatures[:2, 1:])
center = temperatures[:2, 1:3]
print("Центральный фрагмент:\n", center)
print("Форма фрагмента:", center.shape)

# Задание 4. Используются только обычные прямоугольные срезы.
matrix = np.arange(1, 26).reshape(5, 5)
print("\nЗадание 4")
print("Исходная матрица:\n", matrix)
first_rows = matrix[:3, :]
print("Первые три строки:\n", first_rows)
print("Форма:", first_rows.shape)
last_rows = matrix[-2:, :]
print("Последние две строки:\n", last_rows)
print("Форма:", last_rows.shape)
first_columns = matrix[:, :2]
print("Первые два столбца:\n", first_columns)
print("Форма:", first_columns.shape)
fragment = matrix[1:4, 2:5]
print("Строки 1–3, столбцы 2–4:\n", fragment)
print("Форма:", fragment.shape)
corner = matrix[-2:, -2:]
print("Правый нижний блок:\n", corner)
print("Форма:", corner.shape)
