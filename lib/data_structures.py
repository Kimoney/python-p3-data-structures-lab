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
    name_list = [dict_item.get("name", "Not a valid Dictionary KEY") for dict_item in spicy_foods]
    return name_list

def get_spiciest_foods(spicy_foods):
    spiciest_foods = [spiciest for spiciest in spicy_foods if (spiciest.get("heat_level") > 5) ]
    return spiciest_foods

def print_spicy_foods(spicy_foods):
    for foods in spicy_foods:
        food = foods.get("name")
        cuisine = foods.get("cuisine")
        heat = foods.get("heat_level")
        emoji = "🌶"
        print(f"{food} ({cuisine}) | Heat Level: {emoji * heat}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    food_by_cuisine = [food_cuisine for food_cuisine in spicy_foods if (food_cuisine.get("cuisine", "Enter a valid cuisine") == cuisine)]
    for my_dict in food_by_cuisine:
        return my_dict
    

def print_spiciest_foods(spicy_foods):
    spiciest_foods = [spiciest for spiciest in spicy_foods if (spiciest.get("heat_level") > 5)]
    for foods in spiciest_foods:
        food = foods.get("name")
        cuisine = foods.get("cuisine")
        heat = foods.get("heat_level")
        emoji = "🌶"
        print(f"{food} ({cuisine}) | Heat Level: {emoji * heat}")


def get_average_heat_level(spicy_foods):
    heat_level = [heat.get("heat_level") for heat in spicy_foods ]
    list_length = len(heat_level)
    total = sum(heat_level)
    average_heat_level = total / list_length
    return average_heat_level

def create_spicy_food(spicy_foods, spicy_food):
    if type(spicy_food) == dict:
        spicy_foods.append(spicy_food)
        return spicy_foods
    else:
        print("Spicy Food has to ba a dictionary")