print("Задание 5")
max_items = int(input('Введите кол-во предметов: '))
values = list(map(int, input('Введите ценность предметов: ').split()))
positive_values = [x for x in values if x > 0]
positive_values.sort(reverse=True)
selected_items = positive_values[:max_items]
max_value = sum(selected_items)
print(f'Максимальная ценность: {max_value}')