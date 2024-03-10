# Считываем количество игроков
N = int(input("Введите количество игроков: "))

# Считываем ПП каждого игрока
PP_values = []
for i in range(N):
    PP = int(input(f"Введите ПП игрока {i + 1}: "))
    PP_values.append(PP)

# Сортируем ПП игроков
PP_values.sort()

# Инициализируем переменные
i, j = 0, 1
res = 0

# Итерируемся по отсортированному списку
while j < N:
    if PP_values[i] + PP_values[i + 1] >= PP_values[j]:
        j += 1
        current_sum = sum(PP_values[i:j])
        if current_sum > res:
            res = current_sum
    else:
        i += 1

# Выводим результат
print(f"Максимальная сумма ПП игроков: {res}")
