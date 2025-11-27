def is_sorted(arr, i=0):
    # Если дошли до конца или один элемент — массив отсортирован
    if i >= len(arr) - 1:
        return True
    # Если текущая пара нарушает порядок — не отсортирован
    if arr[i] > arr[i + 1]:
        return False
    # Проверяем следующую пару элементов
    return is_sorted(arr, i + 1)
