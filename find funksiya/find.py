# Функция для нахождения максимального из двух чисел
def find_max(a, b):
    if a > b:
        return a
    else:
        return b

# Примеры вызова функции с тремя разными парами чисел
print("Максимум из (5, 10):", find_max(5, 10))
print("Максимум из (22, -3):", find_max(22, -3))
print("Максимум из (7, 7):", find_max(7, 7))


