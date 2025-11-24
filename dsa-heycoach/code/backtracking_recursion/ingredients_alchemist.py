"""
You are a young alchemist on a quest to brew a
magical potion. Each day, you add a specific
number of ingredients to the cauldron. Write a function
to recursively calculate the total number of ingredients
 used to brew the potion over a given number of days.

Input Format:

An integer n, representing the number of days
you have brewed the potion.
An integer ingredientsPerDay, representing
 the number of ingredients added to the cauldron each day.
"""


class AlchemistIngredients:

    def __init__(self, days, ingredients_per_day):
        self.days = days
        self.ingredients_per_day = ingredients_per_day

    def brute_force(self):
        """
        Recursion has no brute force
        """
        return

    def expected_approach(self):
        """
        it returns total number of ingredients for n days
        , for each day it accumulates ingredients_per_day
        """

        def solve(days, ingredients_per_day):
            # description: It returns number of ingredients for given day,
            # each day it accumulates ingredients_per_day
            if days == 1:
                return ingredients_per_day
            return ingredients_per_day + solve(days-1, ingredients_per_day)

        return solve(self.days, self.ingredients_per_day)


if __name__ == "__main__":
    days = 9
    ingredients_per_day = 8
    res = AlchemistIngredients(days, ingredients_per_day)
    print(res.expected_approach())
