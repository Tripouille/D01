from datetime import datetime
from recipe import Recipe


class Book:
    def __init__(self, name="new book"):
        if not isinstance(name, str):
            raise TypeError("book name type must be str")
        if len(name) == 0:
            raise ValueError("name can't be empty")
        self.name = name
        self.creation_date = datetime.now()
        self.last_update = self.creation_date
        self.recipes_list = {"starter": {}, "lunch": {}, "dessert": {}}

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        for key in self.recipes_list:
            if name in self.recipes_list[key]:
                print(self.recipes_list[key][name])
                return (self.recipes_list[key][name])
        raise ValueError("This recipe name is not in this book")

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        if recipe_type not in self.recipes_list:
            raise ValueError("This type is not in your book")
        return (self.recipes_list[recipe_type])

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if not isinstance(recipe, Recipe):
            raise TypeError("recipe must be of type recipe")
        if recipe.name in self.recipes_list[recipe.recipe_type]:
            raise ValueError("this recipe name is already in this book")
        self.recipes_list[recipe.recipe_type][recipe.name] = recipe
        self.last_update = datetime.now()
        print(recipe.name, "added succesfully")
