def gcd(a, b):
    """Функция для нахождения НОД (алгоритм Евклида)"""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Функция для нахождения НОК"""
    return (a * b) // gcd(a, b)

def main():
    # Ввод двух натуральных чисел
    A = int(input("Введите первое натуральное число A: "))
    B = int(input("Введите второе натуральное число B: "))

    # Проверка на натуральные числа
    if A <= 0 or B <= 0:
        print("Пожалуйста, введите натуральные числа больше нуля.")
        return

    # Вычисление НОД и НОК
    nod = gcd(A, B)
    nok = lcm(A, B)

    # Вывод результатов
    print(f"Наибольший общий делитель (НОД) чисел {A} и {B}: {nod}")
    print(f"Наименьшее общее кратное (НОК) чисел {A} и {B}: {nok}")

if _name_ == "_main_":
    main()