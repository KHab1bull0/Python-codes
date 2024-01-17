class Transport:
    def __init__(self, brand: str, model: str, color: str) -> str:
        self.brand = brand
        self.model = model
        self.color = color

    def get_info(self):
        return f"{self.brand} {self.model} { self.color}"

    def set_brand(self, brand):
        self.brand = brand

    def set_model(self, model):
        self.model = model

    def set_color(self, color):
        self.color = color

class Car(Transport):
    def __init__(self,brand: str, model:str, color: str, speed: int, seatcount: int, m_date: int):
        super().__init__(brand, model, color)
        self.speed = speed
        self.seatcount = seatcount
        self.m_date = m_date

    def get_info(self):
        trans = super().get_info()
        return f"{trans} {self.speed} {self.seatcount} {self.m_date}"

    def set_speed(self, speed):
        self.speed = speed
        return self.speed

    def set_speed(self, seatcount):
        self.seatcount = seatcount
        return self.seatcount

    def set_mdate(self, m_date):
        self.m_date = m_date
        return self.m_date

class Truck(Transport):
    def __init__(self, brand: str, model: str, color: str, weight: int):
        super().__init__(brand, model, color)
        self.weight = weight

    def get_info(self):
        info = super().get_info()
        return f"{info} {self.weight} "

    def set_weight(self, weight):
        self.weight = weight

car = Car("Bmw", "M5", "Black", 320, 2, 2022)
truck = Truck("Man", "M3", "white", 5000)

print(car.get_info())
print(truck.get_info())
