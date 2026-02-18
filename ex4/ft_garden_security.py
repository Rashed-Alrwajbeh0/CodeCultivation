class SecurePlant:
    def get_name(self):
        print(f"The plant name is: {self.__name}")

    def get_age(self):
        if self.__age == -1:
            print("Please set the age first")
        else:
            print(f"The plant age is: {self.__age}")

    def set_age(self, age:int):
        if age < 0:
            print(f"Invalid operation attempted: age {age}days [REJECTED]")
            print("Security: Negative age rejected")
            if self.__FirstAge:
                self.__age = -1
        else:
            self.__age = age
            print(f"Age updated: {self.__age} days [OK]")
            if self.__FirstAge:
                self.__FistAge = 0

    def get_height(self):
        if self.__height == -1:
            print("Please set the height first")
        else:
            print(f"The plant height is: {self.__height}")

    def set_height(self, height : int):
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
            if (self.__FirstHeight):
                self.__height = -1
        else:
            self.__height = height
            print(f"Height updated: {self.__height}cm [OK]")
            if self.__FirstHeight:
                self.__FirstHeight = 0

    def __init__(self, name:str, height:int, age:int):
        self.__name = name.capitalize()
        self.__FirstHeight = 1
        self.__FirstAge = 1
        print(f"Plant created: {self.__name}")
        self.set_age(age)
        self.set_height(height)

    def get_info(self):
        print(f"Current plant: {self.__name}" , end=" ")
        print(f"({self.__height}cm, {self.__age} days)")

if __name__ == "__main__":
    print("=== Garden Security System ===")
    p1 = SecurePlant("Rose", 25, 30)
    print("\n")
    p1.set_height(-5)
    print("\n")
    p1.get_info()

