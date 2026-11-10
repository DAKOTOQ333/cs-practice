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

# Задание 5. Изменение сразу нескольких элементов присваиванием срезу.
print("\nЗадание 5")
vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0
print("Пример с вектором:", vector)
small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9
print("Пример с матрицей:\n", small_matrix)

# copy() создаёт независимые данные: изменение копии не меняет оригинал.
# Простое присваивание changed_hours = hours создало бы вторую ссылку
# на тот же массив, поэтому для сохранения hours нужна именно копия.
changed_hours = hours.copy()
changed_hours[2:5] = 99
changed_hours[::2] = -1
print("Изменённый hours:", changed_hours)
print("Исходный hours:", hours)

changed_matrix = matrix.copy()
changed_matrix[1, :] = 0
changed_matrix[:, -1] = -1
changed_matrix[1:4, 1:4] = 100
print("Изменённая матрица:\n", changed_matrix)
print("Исходная матрица:\n", matrix)

# Задание 6. reshape сохраняет количество и порядок элементов.
numbers = np.arange(12)
table = numbers.reshape(3, 4)
transposed = table.T
print("\nЗадание 6")
print("numbers:\n", numbers)
print("Форма numbers:", numbers.shape)
print("table:\n", table)
print("Форма table:", table.shape)
print("transposed:\n", transposed)
print("Форма transposed:", transposed.shape)

# reshape(3, 4) работает: в массиве 12 элементов и 3 * 4 == 12.
# reshape(5, 3) вызовет ValueError: форма требует 15 элементов, а их 12.
# Транспонирование меняет строки и столбцы местами: (3, 4) -> (4, 3).
