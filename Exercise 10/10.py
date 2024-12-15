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

def read_matrix_from_file(filename):
    """Считывает матрицу из файла."""
    with open(filename, 'r') as file:
        lines = file.readlines()
        matrix = [list(map(int, line.split())) for line in lines]
        return np.array(matrix)

def write_results_to_file(filename, max_in_rows, min_in_columns, updated_matrix):
    """Записывает результаты в файл."""
    with open(filename, 'w') as file:
        file.write("Наибольшие элементы в каждой строке:\n")
        file.write(' '.join(map(str, max_in_rows)) + '\n')
        
        file.write("Наименьшие элементы в каждом столбце:\n")
        file.write(' '.join(map(str, min_in_columns)) + '\n')
        
        file.write("Обновленная матрица после замены:\n")
        for row in updated_matrix:
            file.write(' '.join(map(str, row)) + '\n')

def main():
    input_filename = "ФИО_группа_vvod.txt"  # Замените на ваше имя файла
    output_filename = "ФИО_группа_vivod.txt"  # Замените на ваше имя файла
    
    # Считывание матрицы из файла
    matrix = read_matrix_from_file(input_filename)
    
    print("Считанная матрица:")
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
    
    # Запись результатов в файл
    write_results_to_file(output_filename, max_in_rows, min_in_columns, updated_matrix)

if __name__ == "__main__":
    main()
