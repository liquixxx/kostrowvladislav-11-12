def power(x, n):
    # Базовый случай: любая степень 0 даёт 1
    if n == 0:
        return 1
    # Если n отрицательное: x^n = 1 / x^(-n)
    if n < 0:
        return 1 / power(x, -n)
    # Рекурсивный случай: x^n = x * x^(n-1)
    return x * power(x, n - 1)
