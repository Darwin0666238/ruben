def is_prime(n, divisor=None):
    # Базовый случай: если divisor не задан, начнем с 2
    if divisor is None:
        divisor = 2
    
    # Если divisor стал больше квадратного корня из n, число простое
    if divisor * divisor > n:
        return True
    
    # Если n делится на divisor, оно составное
    if n % divisor == 0:
        return False
    
    # Рекурсивный вызов с увеличенным делителем
    return is_prime(n, divisor + 1)

# Основная функция для проверки числа и вывода результата
def check_prime(n):
    if n <= 1:
        return "NO"
    
    if is_prime(n):
        return "YES"
    else:
        return "NO"

# Пример использования
n = int(input("Введите натуральное число n > 1: "))
result = check_prime(n)
print(result)
