import random
from pprint import pprint

def Breakfasts():
    breakfast_Meals = {"What Mummy Makes : Eggy bread - pg 20/23",
    "What Mummy Makes : Mexican baked eggs - pg 24",
    "What Mummy Makes : Scrambled eggs - pg 26",
    "What Mummy Makes : Porridge fingers - pg 20",
    "What Mummy Makes : Berry cheescake bowl - pg 34",
    "What Mummy Makes : Bacon cheese & chive muffins - pg 36",
    "What Mummy Makes : Blueberry oat muffins - pg 37",
    "What Mummy Makes : Banana pancakes - pg 38",
    "What Mummy Makes : Blueberry pancake bites - pg 41"}

    breakfast = random.sample(breakfast_Meals,5)
    pprint(breakfast)

print("\n------------------Breakfast Meals------------------")
#pprint(Breakfast)
Breakfasts()
print("\n")

def Lunches():
    lunch_meals = {"What Mummy Makes : 3 min pasta sauce - pg 46",
    "What Mummy Makes : Cheesy sweet potato & carrot rosti - pg 48",
    "What Mummy Makes : Tortilla roll ups - pg 49",
    "What Mummy Makes : Tortilla / pitta pizza - pg 51",
    "What Mummy Makes : Smokey bean Quesadilla - pg 52",
    "What Mummy Makes : Apple,Courgette & Cheese Quesadilla - pg 52",
    "What Mummy Makes : Avocado cheese toastie - pg 55",
    "What Mummy Makes : Carrot,chive & cheese toastie - pg 55",
    "What Mummy Makes : Chicken noodle soup - pg 56",
    "What Mummy Makes : Cheesy broccoli orzo - pg 59"}

    Lunch = random.sample(lunch_meals,5)
    pprint(Lunch)

print("\n------------------Lunch Meals------------------")
#pprint(Lunch)
Lunches()
print("\n")

def Dinners():
    dinner_meals = {"What Mummy Makes : Hulk Mac n Cheese - pg 68",
    "What Mummy Makes : Cheats beef ragu - pg 71",
    "What Mummy Makes : potato wedges - pg 72",
    "What Mummy Makes : Lemon & garlic sauteed brocolli - pg 77",
    "What Mummy Makes : Lemon & Cheddar chicken bites - pg 78",
    "What Mummy Makes : Sticky seame orange chicken - pg 80",
    "What Mummy Makes : Smokey sweet potato & parsnip wedges - pg 81",
    "What Mummy Makes : Satay chicken dippers - pg 82",
    "What Mummy Makes : Cheats risotto - pg 83",
    "What Mummy Makes : Cheesy Surprise Arancini balls - pg 84",
    "What Mummy Makes : Quick lentil dahl - pg 87",
    "What Mummy Makes : My first curry - pg 88",
    "What Mummy Makes : Chicken fried rice - pg 90",
    "What Mummy Makes : Baby friendly chili con carne - pg 92",
    "What Mummy Makes : Baby friendly lamb kebabs - pg 94",
    "What Mummy Makes : My first stir fry - pg 97",
    "What Mummy Makes : Spinach & chicken open top tart - pg 101",
    "What Mummy Makes : Spinach & ricotta puff parcels - pg 102",
    "What Mummy Makes : Creamy courgette & chicken pasta - pg 117",
    "What Mummy Makes : Lasagne roll ups - pg 120",
    "What Mummy Makes : Cheesy courgette pizza - pg 123",
    "What Mummy Makes : Family friendly fajita - pg 127",
    "What Mummy Makes : Butter chicken - pg 128"}

    Dinner = random.sample(dinner_meals,5)
    pprint(Dinner)

print("\n------------------Dinner Meals------------------")
#pprint(Dinner)
Dinners()
print("\n")

def Freezers():
    freezer_stash = {"What Mummy Makes : Pan fried fritters - pg 132",
    "What Mummy Makes : Shortcut pan fried fritters - pg 135",
    "What Mummy Makes : Quinoa & black bean cups - pg 136",
    "What Mummy Makes : Chicken & Brocoli nuggets - pg 137",
    "What Mummy Makes : Cheesy chive pancakes - pg 138",
    "What Mummy Makes : Sweetcorn & chickpea patties - pg 139",
    "What Mummy Makes : Savoury flapjack - pg 140",
    "What Mummy Makes : Cheesy cornbread muffins - pg 142",
    "What Mummy Makes : Courgette puff pinwheels - pg 145",
    "What Mummy Makes : Broccoli cheese bites - pg 146",
    "What Mummy Makes : Baby friendly skinless sausages - pg 147",
    "What Mummy Makes : Baby friendly meatballs - pg 149",
    "What Mummy Makes : Cornflake chicken dippers - pg 154",
    "What Mummy Makes : Lentil spaghettie bolognese - pg 156"}

    Freezer = random.sample(freezer_stash,5)
    pprint(Freezer)

print("\n------------------Freezer Stash------------------")
#pprint(Freezer)
Freezers()
print("\n")

def Desserts():
    dessert_meals = {"What Mummy Makes : Ginger oat cookies - pg 162",
    "What Mummy Makes : Peanut butter softbake cookies - pg 164",
    "What Mummy Makes : Cinnamon & banana oaty cups - pg 164",
    "What Mummy Makes : Carrot & apple soft oaty bars - pg 165",
    "What Mummy Makes : Peanut butter & banana flapjacks - pg 166",
    "What Mummy Makes : Blueberry sponge fingers - pg 169",
    "What Mummy Makes : Fruit salad with lime youghurt - pg 171",
    "What Mummy Makes : Carrot & raisin muffins - pg 172",
    "What Mummy Makes : Almond & prune muffins - pg 173",
    "What Mummy Makes : Baby bliss balls - pg 174",
    "What Mummy Makes : Chia cheese crackers - pg 176",
    "What Mummy Makes : Seeded oat cakes - pg 177",
    "What Mummy Makes : Spiced soda bread rolls - pg 178",
    "What Mummy Makes : Creamy mango & raspberry ice lollies - pg 179",
    "What Mummy Makes : Chocolate, peanut butter & banana ice cream - pg 180",
    "What Mummy Makes : Berry Banana ice pops - pg 183",
    "What Mummy Makes : Baked bananas - pg 185",
    "What Mummy Makes : Winter spiced poached plums & pears - pg 186",
    "What Mummy Makes : Mini raspberry clafoutis - pg 188",
    "What Mummy Makes : Apple & Blackberry mine galette - pg 191",
    "What Mummy Makes : Semolina pudding - pg 192",
    "What Mummy Makes : Smooth vanilla rice pudding - pg 193",
    "What Mummy Makes : Sweet spiced cous cous pudding - pg 194",
    "What Mummy Makes : Ginger bread biscuits - pg 197",
    "What Mummy Makes : Celebration cake - pg 198"}

    Desserts = random.sample(dessert_meals,5)
    pprint(Desserts)

print("\n------------------Dessert Meals------------------")
#pprint(Desserts)
Desserts()
print("\n")