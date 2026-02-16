class Plant:
    growth_days = 0
    def __init__(self, name: str, hight: int, age: int):
        self.name = name
        self.hight = hight
        self.age = age

    def display(self):
        print(f"{self.name.capitalize()}: {self.hight}cm, {self.age} days old")

    def grow(self):
        self.hight+=1
        self.growth_days+=1

    def  Age(self):
        self.age+=1
if __name__ == "__main__":
    plant = Plant("Rose", 25, 30)
    for x in range(1, 8):
        print(f"=== Day{x} ===")
        plant.display()
        plant.grow()
        plant.Age();
    print(f"Growth this week: +{plant.growth_days - 1}cm")

