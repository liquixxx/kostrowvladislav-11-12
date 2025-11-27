def reverse_string(s):
    # Базовый случай: пустая строка или один символ
    if len(s) <= 1:
        return s
    # Последний символ + разворот оставшейся части
    return s[-1] + reverse_string(s[:-1])

# пример использования
text = "recursion"
print("Исходная строка:", text)
print("Развёрнутая строка:", reverse_string(text))
