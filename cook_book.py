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