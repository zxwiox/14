import random
print("Задание 1")
list = []
for i in range(4):
    row = []
    for j in range(5):
        row.append(random.randint(1,50))
        list.append(row)
print("Список")
for row in list:
    print(row)
max_value  = list[0][0]
max_row = 0
max_col = 0
for i in range(4):
    for j in range(5):
        if list[i][j] > max_value:
            max_value = list[i][j]
            max_row = i
            max_col = j
print(f"Максимальный элемент {max_value} на позиции [{max_row},{max_col}]")