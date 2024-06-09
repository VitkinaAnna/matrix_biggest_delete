import numpy as np

# Приклад матриці (збільшена для перевірки)
matrix = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
    [130, 150, 150, 160]
])

# Крок 1: Знайти найбільше значення M серед елементів під головною діагоналлю
n = matrix.shape[0]
max_value = None
indices = []

# Проходимо по всіх елементах під діагоналлю
for i in range(1, n):
    for j in range(0, i):
        if max_value is None or matrix[i][j] > max_value:
            max_value = matrix[i][j]
            indices = [(i, j)]
        elif matrix[i][j] == max_value:
            indices.append((i, j))

indices_correct = [(i+1, j+1) for i, j in indices]

print(f"Найбільше значення M: {max_value}")
print(f"Індекси елементів з M під діагоналлю: {indices_correct}, ")

# Крок 2: Видалити кожен рядок і стовпець зі значенням M під діагоналлю
rows_to_delete = set(i for i, j in indices)
cols_to_delete = set(j for i, j in indices)

# Видаляємо відповідні рядки та стовпці
new_matrix = np.delete(matrix, list(rows_to_delete), axis=0)
new_matrix = np.delete(new_matrix, list(cols_to_delete), axis=1)

print("Матриця після видалення:")
print(new_matrix)
