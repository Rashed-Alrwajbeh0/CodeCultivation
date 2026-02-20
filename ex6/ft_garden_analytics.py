class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.set_name(name)
        self.set_age(age)
        self.set_height(height)

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_height(self):
        return self.__height

    def set_name(self, name: str):
        self.__name = name

    def set_age(self, age: int):
        while age < 0:
            age = int(input("Please enter a positive age: "))
        self.__age = age

    def set_height(self, height: int):
        while height < 0:
            height = int(input("Please enter a positive height: "))
        self.__height = height


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.set_color(color)
        self.set_blooming(True)

    def get_color(self):
        return self.__color

    def get_blooming(self):
        return self.__blooming

    def set_color(self, color: str):
        self.__color = color

    def set_blooming(self, blooming: bool):
        self.__blooming = blooming


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, age: int,
                 color: str, points: int):
        super().__init__(name, height, age, color)
        self.set_points(points)

    def get_points(self):
        return self.__points

    def set_points(self, points: int):
        while points < 0:
            points = int(input("Please enter a positive points: "))
        self.__points = points


class Garden:
    def __init__(self, manager: str):
        self.__manager = manager
        self.__plants = []
        self.__plants_species = []
        self.__number_of_plants = 0
        self.__growth = 0

    def add_plant(self, species: str, name: str, height: int, age: int,
                  color: str = None, points: int = 0):
        s = species.capitalize()
        if s != "Plant" and s != "Floweringplant" and s != "Prizeflower":
            print("The type must be Plant or FloweringPlant or PrizeFlower\n")
        else:
            if s == "Plant":
                self.__plants.append(Plant(name, height, age))
                self.__plants_species.append("Plant")
            elif s == "Floweringplant":
                self.__plants.append(FloweringPlant(name, height, age, color))
                self.__plants_species.append("FloweringPlant")
            else:
                self.__plants.append(PrizeFlower(name, height, age,
                                     color, points))
                self.__plants_species.append("PrizeFlower")

            print(f"Added {name} to {self.__manager}'s garden")
            self.__number_of_plants += 1

    def grow_all(self, num: int):
        print(f"{self.__manager} is helping all plants grow...")
        for i in self.__plants:
            self.__growth += num
            i.set_height(i.get_height() + num)
            print(f"{i.get_name()} grew {num}cm")

    def calculate_score(self):
        ans = 0
        for i in range(len(self.__plants)):
            ans += self.__plants[i].get_height()
            if self.__plants_species[i] == "PrizeFlower":
                ans += self.__plants[i].get_points()
        return ans

    class statistics:
        def __init__(self, name, number_of_plants, plants,
                     plants_species, g, s):
            self.__plants = plants
            self.__number_of_plants = number_of_plants
            self.__plants_species = plants_species
            self.__name = name
            self.__growth = g
            self.__score = s
            self.__num_of_plant = 0
            self.__num_of_floweringplan = 0
            self.__num_of_prizeflower = 0

        def calc_plants(self):
            for i in self.__plants_species:
                if i.capitalize() == "Plant":
                    self.__num_of_plant += 1
                elif i.capitalize() == "Floweringplant":
                    self.__num_of_floweringplan += 1
                else:
                    self.__num_of_prizeflower += 1

        def print_info(self):
            print(f"=== {self.__name}'s Garden Report ===")
            for i in range(len(self.__plants)):
                p = self.__plants[i]
                spec = self.__plants_species[i]
                print(f"- {p.get_name()}: {p.get_height()}cm", end="")
                if spec != "Plant":
                    bloom = "blooming" if p.get_blooming() else "not blooming"
                    print(f", {p.get_color()} flowers ({bloom})", end="")
                if spec == "PrizeFlower":
                    print(f", Prize points: {p.get_points()}", end="")
                print()

            print(f"Plants added: {self.__number_of_plants}, "
                  f"Total growth: {self.__growth}cm")
            self.calc_plants()
            print(f"Plant types: {self.__num_of_plant} regular, "
                  f"{self.__num_of_floweringplan} flowering, "
                  f"{self.__num_of_prizeflower} prize flowers")
            GardenManager.test_height(2)
            print(f"Garden scores - {self.__name} : {self.__score}")


class GardenManager:
    __counter = 0

    def __init__(self, owner: str):
        self.__owner = owner
        self.__managers = []
        self.__managers_names = []
        GardenManager.__counter += 1

    def add_manager(self, name):
        self.__managers_names.append(name)
        self.__managers.append(Garden(name))

    @classmethod
    def get_counter(cls):
        return f"Total gardens managed: {cls.__counter}"

    def add_plant(self, manager: str, species: str, name: str, height: int,
                  age: int, color: str = None, points: int = 0):
        if self.check_manager(manager, self.__managers_names):
            idx = self.__managers_names.index(manager)
            self.__managers[idx].add_plant(species, name,
                                           age, height, color, points)
        else:
            print("This manager does not exist")

    def check_manager(self, name: str, names: list):
        return name in names

    def grow_all(self, name: str, num: int):
        if self.check_manager(name, self.__managers_names):
            idx = self.__managers_names.index(name)
            self.__managers[idx].grow_all(num)
        else:
            print("This manager does not exist")

    def show_report(self, manager_name: str):
        idx = self.__managers_names.index(manager_name)
        g = self.__managers[idx]
        stats_obj = Garden.statistics(
            manager_name,
            len(g._Garden__plants),
            g._Garden__plants,
            g._Garden__plants_species,
            g._Garden__growth,
            g.calculate_score()
        )
        stats_obj.print_info()

    @staticmethod
    def test_height(height: int):
        print(f"Height validation test: {height > 0}")


if __name__ == "__main__":
    manager = GardenManager("Rashed")
    manager.add_manager("Alice")

    print("=== Garden Management System Demo ===")

    manager.add_plant("Alice", "Plant", "Oak Tree", 100, 10)
    manager.add_plant("Alice", "FloweringPlant", "Rose", 25, 2, "red")
    manager.add_plant("Alice", "PrizeFlower", "Sunflower", 50, 1, "yellow", 10)

    manager.grow_all("Alice", 2)
    manager.show_report("Alice")

    print(manager.get_counter())
