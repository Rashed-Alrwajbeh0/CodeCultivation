class Plant:
    def __init__(self, name: str, hight: int, age: int):
        self.name = name
        self.hight = hight
        self.age = age

    def display(self):
        print(f"{self.name.capitalize()}: {self.hight}cm, {self.age} days old")


if __name__ == "__main__":
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Sunflower", 80, 45)
    plant3 = Plant("Cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    plant1.display()
    plant2.display()
    plant3.display()
