def generate_binary(n, prefix=""):
    # Если длина строки уже n — выводим
    if len(prefix) == n:
        print(prefix)
        return
    # Добавляем 0
    generate_binary(n, prefix + "0")
    # Добавляем 1
    generate_binary(n, prefix + "1")

# пример использования
print("Бинарные строки длины 3:")
generate_binary(3)
