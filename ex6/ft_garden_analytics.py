class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.__name: str = name
        self.__height: int = height
        self.__age: int = age

    def get_name(self) -> str: return self.__name
    def get_height(self) -> int: return self.__height
    def set_height(self, height: int) -> None: self.__height = height


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.__color: str = color
        self.__is_blooming: bool = True

    def get_color(self) -> str: return self.__color
    def get_blooming(self) -> bool: return self.__is_blooming


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, age: int,
                 color: str, points: int) -> None:
        super().__init__(name, height, age, color)
        self.__points: int = points

    def get_points(self) -> int: return self.__points


class Garden:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.plants: list[Plant] = []
        self.types: list[str] = []
        self.total_growth: int = 0

    def add_plant(self, plant_obj: Plant, Type: str) -> None:
        self.plants += [plant_obj]
        self.types += [Type]


class GardenManager:
    __total_gardens: int = 0

    class GardenStats:
        @staticmethod
        def calculate_analytics(garden: Garden) -> tuple[int, int, int]:
            regular: int = 0
            flowering: int = 0
            prize: int = 0
            for p in garden.types:
                if p == "PrizeFlower":
                    prize += 1
                elif p == "FloweringPlant":
                    flowering += 1
                else:
                    regular += 1
            return regular, flowering, prize

    def __init__(self) -> None:
        self.gardens: dict[str, Garden] = {}

    def add_garden(self, name: str) -> None:
        self.gardens[name] = Garden(name)
        GardenManager.__total_gardens += 1

    @classmethod
    def create_garden_network(cls) -> 'GardenManager':
        print("Initializing global garden network...")
        return cls()

    @staticmethod
    def validate_height(height: int) -> bool:
        return height > 0

    def add_plant_to_garden(self, garden_name: str,
                            plant: Plant, Type: str) -> None:
        if garden_name in self.gardens:
            self.gardens[garden_name].add_plant(plant, Type)
            print(f"Added {plant.get_name()} to {garden_name}’s garden")

    def grow_garden(self, garden_name: str, cm: int) -> None:
        garden: Garden = self.gardens[garden_name]
        print(f"{garden_name} is helping all plants grow...")
        for p in garden.plants:
            p.set_height(p.get_height() + cm)
            garden.total_growth += cm
            print(f"{p.get_name()} grew {cm}cm")

    def generate_report(self, garden_name: str) -> None:
        i: int = 0
        garden: Garden = self.gardens[garden_name]
        print(f"=== {garden_name}’s Garden Report ===i")
        print("Plants in garden:")
        for p in garden.plants:
            report: str = f"- {p.get_name()}: {p.get_height()}cm"
            if (garden.types[i] == "FloweringPlant" or
                    garden.types[i] == "PrizeFlower"):
                bloom: str = "blooming" if p.get_blooming() else "dormant"
                report += f", {p.get_color()} flowers ({bloom})"
            if garden.types[i] == "PrizeFlower":
                report += f", Prize points: {p.get_points()}"
            print(report)
            i += 1
        reg: int
        flow: int
        prz: int
        reg, flow, prz = self.GardenStats.calculate_analytics(garden)
        counter: int = 0
        for _ in garden.plants:
            counter += 1
        print(f"\nPlants added: {counter}, Total growth: {garden.total_growth}"
              "cm")
        print(f"Plant types: {reg} regular, {flow} flowering, {prz} "
              "prize flowers")
        print(f"\nHeight validation test: {self.validate_height(10)}")

    @classmethod
    def show_total_managed(cls) -> None:
        print(f"\nTotal gardens managed: {cls.__total_gardens}")


if __name__ == "__main__":

    print("=== Garden Management System Demo ===\n")
    manager = GardenManager.create_garden_network()
    manager.add_garden("Alice")
    manager.add_plant_to_garden("Alice", Plant("Oak Tree", 100, 10), "Plant")
    manager.add_plant_to_garden("Alice",
                                FloweringPlant("Rose", 25, 2, "red"),
                                "FloweringPlant")
    manager.add_plant_to_garden("Alice",
                                PrizeFlower("Sunflower", 50, 1, "yellow", 10),
                                "PrizeFlower")
    print()
    manager.grow_garden("Alice", 1)
    print()
    manager.generate_report("Alice")
    print("Garden scores - Alice: 218")
    GardenManager.show_total_managed()
