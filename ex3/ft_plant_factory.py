class Plant:
    total = 0

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
        Plant.total += 1
        print(f"Created: {self.name.capitalize()}", end=" ")
        print(f"({self.height}cm, {self.age} days)")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Sunflower", 80, 45)
    plant3 = Plant("Cactus", 5, 90)
    plant4 = Plant("Oak", 200, 365)
    plant5 = Plant("Fern", 15, 120)
    print(f"Total plants created: {Plant.total}")
