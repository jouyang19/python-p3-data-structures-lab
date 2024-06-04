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
    names = []
    for food in spicy_foods:
        names.append(food['name'])
    return names

def get_spiciest_foods(spicy_foods):
    spiciestArr = []
    for food in spicy_foods:
        if food['heat_level'] > 5:
            spiciestArr.append(food)
    return spiciestArr

get_spiciest_foods(spicy_foods)

def print_spicy_foods(spicy_foods):
    new_list = []
    for food in spicy_foods:
        name = food['name']
        cuisine = food['cuisine']
        heat_level = food['heat_level'] * "🌶"
        (new_list.append(f'{name} ({cuisine}) | Heat Level: {heat_level}'))
    for item in new_list:
        print(item)
    
print_spicy_foods(spicy_foods)
        
        

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food
        else:
            None
print(get_spicy_food_by_cuisine(spicy_foods, 'American'))
print(get_spicy_food_by_cuisine(spicy_foods, 'Thai'))
print(get_spicy_food_by_cuisine(spicy_foods, 'Sichuan'))

def print_spiciest_foods(spicy_foods):
    new_list = []
    for food in spicy_foods:
        if food['heat_level'] > 5:
            name = food['name']
            cuisine = food['cuisine']
            heat_level = food['heat_level'] * '🌶'
            new_list.append(f'{name} ({cuisine}) | Heat Level: {heat_level}')
    else:
        None
    for item in new_list:
        print(item)
print_spiciest_foods(spicy_foods)

def get_average_heat_level(spicy_foods):
    sum = 0
    for food in spicy_foods:
        sum = sum + food['heat_level']
    return sum / len(spicy_foods)
get_average_heat_level(spicy_foods)
        
        
spicy_food = {
    'name': 'Griot',
    'cuisine': 'Haitian',
    'heat_level': 10
}

def create_spicy_food(spicy_foods, spicy_food):
    new_spicy_foods = spicy_foods
    new_spicy_foods.append(spicy_food)
    return new_spicy_foods
print(create_spicy_food(spicy_foods, spicy_food))
