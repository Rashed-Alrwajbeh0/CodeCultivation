class Plant:
    growth_days = 0

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def display(self) -> None:
        print(f"{self.name.capitalize()}: {self.height}cm, {self.age} days old")

    def grow(self) -> None:
        self.height += 1
        self.growth_days += 1

    def age(self) -> None:
        self.age += 1


if __name__ == "__main__":
    plant = Plant("Rose", 25, 30)
    for x in range(1, 8):
        print(f"=== Day{x} ===")
        plant.display()
        plant.grow()
        plant.age()
    print(f"Growth this week: +{plant.growth_days - 1}cm")
