class Soldat:
    def __init__(self,name,tall,weight,age,gender) -> None:
        self.name = name
        self.tall = tall
        self.weight = weight
        self.age = age
        self.gender = gender

    def get_name(self):
        return self.name

    def get_weight(self):
        return self.weight

    def get_tall(self):
        return self.tall

    def get_age(self):
        return self.age

    def get_gender(self):
        return self.gender


class Armiya(Soldat):
    soldanList = []
    tankList = []
    def __init__(self,name, tall, weight, age, gender) -> None:
        super().__init__(name, tall, weight, age, gender)

    def check_soldan_age(self):
        age = super().get_age()
        gender = super().get_gender()
        tall = super().get_tall()
        weight = super().get_weight()

        if age > 18 and gender == 'Erkak':
            if tall < 150 and weight < 75:
                self.soldanList.append(f"Ismi: {self.name}, Bo'yi: {tall}, Vazni: {weight}, Yoshi: {age}, Jinsi: {gender}")
            else:
                self.tankList.append(f"Ismi: {self.name}, Bo'yi: {tall}, Vazni: {weight}, Yoshi: {age}, Jinsi: {gender}")


    def get_info_piyoda(self):
        print("Piyoda askarlar.")
        for i in self.soldanList:
            print(i)

    def get_info_tank(self):
        print("Tank askarlar.")
        for i in self.tankList:
            print(i)



armiya = Armiya('Eshmat',160,80,20,'Erkak')
armiya1 = Armiya('Toshmat',160,80,35,'Ayol')
armiya2 = Armiya('ASDF',160,80,19,'Erkak')
armiya3 = Armiya('CVB',140,60,35,'Erkak')

armiya.check_soldan_age()
armiya1.check_soldan_age()
armiya2.check_soldan_age()
armiya3.check_soldan_age()

armiya.get_info_tank()
armiya.get_info_piyoda()
