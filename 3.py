import random
print("Задача 3")
rows = 4
cols = 5
list = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(random.randint(-20, 20))
    list.append(row)
print("список:")
for row in list:
    print(row)
filtered_list = []
for i in range(len(list)):
    filtered_row = []
    for j in range(len(list[i])):
        if list[i][j] > 0:
            filtered_row.append(list[i][j])
    filtered_list.append(filtered_row)
print("только положительные элементы:")
for row in filtered_list:
    print(row)