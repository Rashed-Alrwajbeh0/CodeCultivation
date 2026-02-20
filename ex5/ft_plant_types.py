class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.age = age
        self.height = height

    def get_info(self) -> None:
        return f"{self.height}cm, {self.age} days,"


class Flower (Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")

    def get_info(self) -> None:
        print(f"{self.name} (Flower): ", end="")
        print(super().get_info(), f"{self.color} color")


class Tree (Plant):
    def __init__(self, name: str, height: int, age: int, t_d: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = t_d

    def produce_shade(self) -> None:
        shade = int(self.trunk_diameter * 1.5)
        print(f"{self.name} provides {shade} square meters of shade")

    def get_info(self) -> None:
        print(f"{self.name} (Tree):", end=" ")
        print(super().get_info(), f"{self.trunk_diameter}cm diameter")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int, harvest_season: str,
                 nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self) -> None:
        print(f"{self.name} (Vegetable):", super().get_info(), end="")
        print(f"{self.harvest_season} harvest")
        print(self.name, self.nutritional_value)


if __name__ == "__main__":
    flower1 = Flower("Rose", 25, 30, "red")
    flower2 = Flower("Sunflower", 80, 45, "yellow")
    tree1 = Tree("Oak", 500, 1825, 50)
    tree2 = Tree("Pine", 300, 1500, 35)
    veg1 = Vegetable("Tomato", 80, 90, "summer", "rich in vitamin C")
    veg2 = Vegetable("Carrot", 40, 70, "winter", "high in vitamin A")
    print("=== Garden Plant Types ===\n")
    flower1.get_info()
    flower1.bloom()
    print("\n")
    tree1.get_info()
    tree1.produce_shade()
    print("\n")
    veg1.get_info()
