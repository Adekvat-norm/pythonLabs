N = int(input("Введите количество игроков: "))
PP_values = []
for i in range(N):
    PP = int(input(f"Введите ПП игрока {i + 1}: "))
    PP_values.append(PP)
PP_values.sort()

i, j = 0, 1
res = 0
maxPP_users = []

while j < N:
    if PP_values[i] + PP_values[i + 1] >= PP_values[j]:
        j += 1
        current_sum = sum(PP_values[i:j])
        if current_sum > res:
            res = current_sum;
            maxPP_users = PP_values[i:j]
    else:
        i += 1

print(f"Максимальная сумма ПП игроков: {res}")
print(f"Игроки с наибольшим вкладом: {maxPP_users}")