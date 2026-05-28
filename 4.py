import random
print("Задача 4")
rows = 4
cols = 5
list = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(random.randint(0, 10))
    list.append(row)
print("список:")
for row in list:
    print(row)
search_value = 5
positions = []
for i in range(len(list)):
    for j in range(len(list[i])):
        if list[i][j] == search_value:
            positions.append([i, j])
if positions:
    print(f"Элемент {search_value} найден на позициях:")
    for pos in positions:
        print(f"[{pos[0]}][{pos[1]}]")
else:
    print(f"Элемент {search_value} не найден")