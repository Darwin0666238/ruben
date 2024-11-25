# Шаг 1: Считываем массив из 10 целых чисел
array = []
print("Введите 10 целых чисел:")
for i in range(10):
    number = int(input(f"Число {i + 1}: "))
    array.append(number)

# Шаг 2: Вычисляем среднее арифметическое
average = sum(array) / len(array)
print(f"Среднее арифметическое: {average}")

# Шаг 3: Подсчитываем количество элементов
max_element = max(array)
count_less_max = sum(1 for x in array if x < max_element)
count_greater_average = sum(1 for x in array if x > average)

print(f"Количество элементов меньше максимального: {count_less_max}")
print(f"Количество элементов больше среднего арифметического: {count_greater_average}")

# Шаг 4: Суммируем числа, которые больше 5
sum_greater_than_5 = sum(x for x in array if x > 5)
print(f"Сумма чисел, которые больше 5: {sum_greater_than_5}")
