import numpy as np

def create_matrix(n):
    """Создание случайной квадратной матрицы размером n x n."""
    return np.random.randint(1, 101, size=(n, n))

def find_max_in_rows(matrix):
    """Находит наибольший элемент в каждой строке."""
    return np.max(matrix, axis=1)

def find_min_in_columns(matrix):
    """Находит наименьший элемент в каждом столбце."""
    return np.min(matrix, axis=0)

def average_of_diagonals(matrix):
    """Находит средний элемент среди элементов главной и побочной диагоналей."""
    main_diag = [matrix[i][i] for i in range(len(matrix))]
    secondary_diag = [matrix[i][len(matrix) - 1 - i] for i in range(len(matrix))]
    
    all_diagonal_elements = main_diag + secondary_diag
    return sum(all_diagonal_elements) / len(all_diagonal_elements)

def swap_diagonal_elements(matrix):
    """Заменяет средний элемент среди диагоналей с элементом на их пересечении."""
    n = len(matrix)
    
    # Находим средний элемент
    avg_elem = average_of_diagonals(matrix)
    
    # Пересечение диагоналей
    intersection_elem = matrix[n // 2][n // 2]
    
    # Меняем местами
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == avg_elem:
                matrix[i][j] = intersection_elem
                matrix[n // 2][n // 2] = avg_elem
                return matrix

def main():
    n = int(input("Введите размер квадратной матрицы (n x n): "))
    
    # Создание матрицы
    matrix = create_matrix(n)
    
    print("Сгенерированная матрица:")
    print(matrix)
    
    # Нахождение наибольших элементов в строках и наименьших в столбцах
    max_in_rows = find_max_in_rows(matrix)
    min_in_columns = find_min_in_columns(matrix)
    
    print("\nНаибольшие элементы в каждой строке:")
    print(max_in_rows)
    
    print("\nНаименьшие элементы в каждом столбце:")
    print(min_in_columns)
    
    # Замена среднего элемента диагоналей
    updated_matrix = swap_diagonal_elements(matrix)
    
    print("\nОбновленная матрица после замены:")
    print(updated_matrix)

if _name_ == "_main_":
    main()
