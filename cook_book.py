#Задание №1
recipe_book = r'C:\Users\Lenovo\Desktop\cookbook\recipes.txt'

with open(recipe_book, 'r', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        name_dish = line.strip()
        meal_count = file.readline()
        meal_list = []
        for i in range(int(meal_count)):
            num = file.readline().strip()
            ingredient_name, quantity, measure = num.split(' | ')
            meal_list.append({
                'ingredient_name': ingredient_name,
                'quantity': int(quantity),
                'measure': measure
            })
        file.readline()
        cook_book[name_dish] = meal_list
    print('cook_book =', cook_book)

#Задание №2
def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for el in cook_book[dish]:
                if el['ingredient_name'] in shop_list:
                    shop_list[el['ingredient_name']]['quantity'] += el['quantity'] * person_count
                else:
                    shop_list[el['ingredient_name']] = {'measure': el['measure'],'quantity': (el['quantity'] * person_count)}
        else:
            print('Такого блюда нет в книге')
    return print('Список продуктов:', shop_list)

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

#Задание №3
with open(r'C:\Users\Lenovo\Desktop\cookbook\1.txt', 'r', encoding='utf-8') as f1:
    content1 = f1.readlines()
with open(r'C:\Users\Lenovo\Desktop\cookbook\2.txt', 'r', encoding='utf-8') as f2:
    content2 = f2.readlines()
with open(r'C:\Users\Lenovo\Desktop\cookbook\3.txt', 'r', encoding='utf-8') as f3:
    content3 = f3.readlines()


files = [('1.txt', len(content1)), ('2.txt', len(content2)), ('3.txt', len(content3))]
files_sorted = sorted(files, key=lambda x: x[1])

with open(r'C:\Users\Lenovo\Desktop\cookbook\result.txt', 'w') as f:
    for file_info in files_sorted:
        f.write(file_info[0] + '\n')
        f.write(str(file_info[1]) + '\n')
        if file_info[0] == '1.txt':
            f.writelines(content1)
        elif file_info[0] == '2.txt':
            f.writelines(content2)
        elif file_info[0] == '3.txt':
            f.writelines(content3)
        f.write('\n')