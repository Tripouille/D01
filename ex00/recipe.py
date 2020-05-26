
class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time,
                 ingredients, description, recipe_type):
        if not isinstance(name, str):
            raise TypeError("Recipe name type must be str")
        if len(name) == 0:
            raise ValueError("recipe name can't be empty")
        if not isinstance(cooking_lvl, int):
            raise TypeError("recipe cooking_lvl type must be int")
        if not 0 < cooking_lvl < 6:
            raise ValueError("recipe cooking_lvl must be >= 1 and <= 5")
        if not isinstance(cooking_time, int):
            raise TypeError("recipe cooking_time type must be int")
        if cooking_time < 0:
            raise ValueError("recipe cooking_time must be positiv")
        if not isinstance(ingredients, list):
            raise TypeError("recipe ingredients type must be list")
        if not all(map(lambda i: isinstance(i, str) and len(i), ingredients)):
            raise ValueError("ingredients list is invalid")
        if not isinstance(description, str):
            raise TypeError("recipe description type must be str")
        if not isinstance(recipe_type, str):
            raise TypeError("recipe_type type must be str")
        if recipe_type not in ["starter", "lunch", "dessert"]:
            raise ValueError("recipe_type must be starter, lunch or dessert")
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    def __str__(self):
        txt = "Recipe name: {}\n".format(self.name)
        txt += "cooking level: {}\n".format(self.cooking_lvl)
        txt += "cooking time: {}\n".format(self.cooking_time)
        txt += "ingredients: {}\n".format(self.ingredients)
        txt += "description: {}\n".format(self.description)
        txt += "recipe type: {}\n".format(self.recipe_type)
        return (txt)
