def power(x, n):
    # Базовый случай: степень 0 даёт 1
    if n == 0:
        return 1
    # Обработка отрицательной степени
    if n < 0:
        return 1 / power(x, -n)
    # Рекурсивный случай: x^n = x * x^(n-1)
    return x * power(x, n - 1)

# пример использования
print("power(2, 5) =", power(2, 5))
print("power(3, -2) =", power(3, -2))
