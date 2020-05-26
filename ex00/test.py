from book import Book
from recipe import Recipe
from time import sleep
import traceback


myBook = Book("Tripouille book's")
print("last update = ", myBook.last_update)
sleep(0.5)
myBook.add_recipe(Recipe("Salade des romains", 1, 15,
                  ["poulet", "salade", "parmesan", "crouton"],
                   "miam", "starter"))
sleep(0.5)
print("last update = ", myBook.last_update)
myBook.add_recipe(Recipe("Burger", 1, 15,
                  ["Boeuf", "fromage", "bacon", "sauce"],
                   "miam", "lunch"))
sleep(0.5)
print("last update = ", myBook.last_update)
myBook.add_recipe(Recipe("Cookies", 1, 15,
                  ["beurre", "farine", "chocolat", "sucre", "oeufs"],
                   "miam", "dessert"))
sleep(0.2)
print("last update = ", myBook.last_update)
myBook.get_recipe_by_name("Salade des romains")
myBook.get_recipe_by_name("Burger")
myBook.get_recipe_by_name("Cookies")

print("Test de get recipe by types avec starter")
for recipe in myBook.get_recipes_by_types("starter"):
    myBook.get_recipe_by_name(recipe)

try:
    myBook.get_recipes_by_types("error")
except Exception:
    traceback.print_exc()
try:
    print(myBook.get_recipe_by_name("test"))
except Exception:
    traceback.print_exc()
try:
    myBook.add_recipe(Recipe("", 1, 15, ["oeufs"],
                             "miam", "dessert"))
except Exception:
    traceback.print_exc()
try:
    myBook.add_recipe(Recipe("Poulet", 6, 15,
                             ["oeufs"], "miam", "dessert"))
except Exception:
    traceback.print_exc()
