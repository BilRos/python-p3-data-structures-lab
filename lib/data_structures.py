import copy
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
    names = [food.get('name') for food in spicy_foods]
    return(names)
get_names(spicy_foods)


def get_spiciest_foods(spicy_foods):
    spiciest = [food for food in spicy_foods if food['heat_level'] > 5]
    return spiciest



def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level_emojis = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emojis}")


def get_average_heat_level(spicy_foods):
    heat_levels = [food.get('heat_level') for food in spicy_foods]
    return sum(heat_levels) / len(heat_levels)
print(get_average_heat_level(spicy_foods))


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food
print(get_spicy_food_by_cuisine(spicy_foods, "American"))

def print_spiciest_foods(spicy_foods):
    spicy = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spicy)
print(print_spiciest_foods(spicy_foods))


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
print(create_spicy_food(spicy_foods, {"name": "Griot", "cuisine": "Haitian", "heat_level":10}))


    