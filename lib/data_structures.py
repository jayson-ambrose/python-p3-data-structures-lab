spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):

    spicy_food_list = []

    for food in spicy_foods:
        spicy_food_list.append(food['name'])

    return spicy_food_list

def get_spiciest_foods(spicy_foods):

    index = 0

    spiciest_food_list = []

    while(index < len(spicy_foods)):

        if spicy_foods[index]['heat_level'] >= 5:
            spiciest_food_list.append(spicy_foods[index])
            
        index += 1

    return spiciest_food_list

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}") 

print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):

    index = 0

    while(index < len(spicy_foods)):

        if spicy_foods[index]['cuisine'] == cuisine:
            return spicy_foods[index]

        index += 1

    return "no foods of that cuisine"

print(get_spicy_food_by_cuisine(spicy_foods, "American"))

def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)

    for food in spiciest_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}") 
    pass

def get_average_heat_level(spicy_foods):

    sum=0

    for food in spicy_foods:
        sum = sum + food['heat_level']

    return  sum / len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
