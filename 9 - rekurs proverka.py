def is_sorted(arr, i=0):
    # Если дошли до конца — массив отсортирован
    if i >= len(arr) - 1:
        return True
    # Если текущая пара нарушает порядок — не отсортирован
    if arr[i] > arr[i + 1]:
        return False
    # Проверяем дальше
    return is_sorted(arr, i + 1)

# примеры использования
a1 = [1, 2, 3, 4, 5]
a2 = [3, 1, 4, 2]

print(a1, "отсортирован?", is_sorted(a1))
print(a2, "отсортирован?", is_sorted(a2))
