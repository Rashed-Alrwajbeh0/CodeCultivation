class SecurePlant:
    def get_name(self) -> None:
        print(f"The plant name is: {self.__name}")

    def get_age(self) -> None:
        if self.__age == -1:
            print("Please set the age first")
        else:
            print(f"The plant age is: {self.__age}")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"Invalid operation attempted: age {age}days [REJECTED]")
            print("Security: Negative age rejected")
            if self.__first_age:
                self.__age = -1
        else:
            self.__age = age
            print(f"Age updated: {self.__age} days [OK]")
            if self.__first_age:
                self.__first_age = 0

    def get_height(self) -> None:
        if self.__height == -1:
            print("Please set the height first")
        else:
            print(f"The plant height is: {self.__height}")

    def set_height(self, height: int) -> None:
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
            if (self.__first_height):
                self.__height = -1
        else:
            self.__height = height
            print(f"Height updated: {self.__height}cm [OK]")
            if self.__first_height:
                self.__first_height = 0

    def __init__(self, name: str, height: int, age: int) -> None:
        self.__name = name.capitalize()
        self.__first_height = 1
        self.__first_age = 1
        print(f"Plant created: {self.__name}")
        self.set_age(age)
        self.set_height(height)

    def get_info(self) -> None:
        print(f"Current plant: {self.__name}", end=" ")
        print(f"({self.__height}cm, {self.__age} days)")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    p1 = SecurePlant("Rose", 25, 30)
    print("\n")
    p1.set_height(-5)
    print("\n")
    p1.get_info()
