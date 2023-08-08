from typing import List


class PizzaPlatter:
    def __init__(self, size: str, crust_type: str, toppings: List[str]):
        self.size = size
        self.crust_type = crust_type
        self.toppings = toppings

    def __str__(self):
        toppings = []
        for topping in self.toppings:
            toppings.append(topping.capitalize())

        return f"Size: {self.size}, Crust Type: {self.crust_type}, Toppings: {', '.join(toppings)}"


class PizzaBuilder:
    def __init__(self, size: str):
        self.size = size
        self.cheese = False
        self.pepperoni = False
        self.mushrooms = False
        self.onions = False
        self.tomatoes = False
        self.crust_type = "regular"

    def add_cheese(self) -> 'PizzaBuilder':
        self.cheese = True
        return self

    def add_pepperoni(self) -> 'PizzaBuilder':
        self.pepperoni = True
        return self

    def add_mushrooms(self) -> 'PizzaBuilder':
        self.mushrooms = True
        return self

    def add_onions(self) -> 'PizzaBuilder':
        self.onions = True
        return self

    def add_tomatoes(self) -> 'PizzaBuilder':
        self.tomatoes = True
        return self

    def set_crust_type(self, crust_type: str) -> 'PizzaBuilder':
        self.crust_type = crust_type
        return self

    def build(self) -> PizzaPlatter:
        toppings = []
        if self.cheese:
            toppings.append("Cheese")
        if self.pepperoni:
            toppings.append("Pepperoni")
        if self.mushrooms:
            toppings.append("Mushrooms")
        if self.onions:
            toppings.append("Onions")
        if self.tomatoes:
            toppings.append("Tomatoes")

        return PizzaPlatter(self.size, self.crust_type, toppings)


def main() -> None:

    # Get the desired pizza size and crust type from the user.
    size = input("What size pizza do you want? (large or thin): ")
    crust_type = input("What crust type do you want? (regular or thin): ")

    # Create a pizza builder based on the user's choices.
    pizza_builder = PizzaBuilder(size)

    pizza_builder.set_crust_type(crust_type)

    # Add the desired toppings to the pizza.
    pizza_builder.add_cheese()
    pizza_builder.add_pepperoni()
    pizza_builder.add_mushrooms()
    pizza_builder.add_onions()
    pizza_builder.add_tomatoes()

    # Build the pizza and print it to the console.
    pizza = pizza_builder.build()
    print(pizza)


if __name__ == '__main__':
    main()
