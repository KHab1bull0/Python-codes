class Cars:
    def __init__(self, id: int, name: str, lastname: str, gender: str, brand: str, year: int, color: str, country: str):
        self.id = id
        self.name = name
        self.lastname = lastname
        self.gender = gender
        self.brand = brand
        self.year = year
        self.color = color
        self.country = country


    def metod1(self, lis):
        lis1 = []
        erke = 0
        ayol = 0

        for i in lis:
            if i.gender == "Erkak":
                erke += 1
            elif i.gender == "Ayol":
                ayol += 1
        sum = erke + ayol

        erke = (erke / sum) * 100
        ayol = (ayol / sum) * 100
        if erke > ayol:
            print("Erkaklar ayollarga nisbatan {0} % ko'p".format(erke))
        else:
            print(f"Ayollar erkaklarga nisbatan {ayol} % ko'p")


lis = []
# n = int(input("Input: "))
# for i in range(n):
#     odam = Cars(int(int(input("Id: "))), input("Name: "), input("Lastname: "), input("Gender: "), input("Brand: "), int(input("Year: ")), input("Color: "), input("Country: "))
odam = Cars(1234, "asdf", 'asdfga', 'Erkak', 'asdfga', 1234, 'asdgfa','asdga')
lis.append(odam)
odam = Cars(1234, "asdf", 'asdfga', 'Ayol', 'asdfga', 1234, 'asdgfa','asdga')
lis.append(odam)
odam = Cars(1234, "asdf", 'asdfga', 'Ayol', 'asdfga', 1234, 'asdgfa','asdga')
lis.append(odam)
odam = Cars(1234, "asdf", 'asdfga', 'Erkak', 'asdfga', 1234, 'asdgfa','asdga')
lis.append(odam)
odam = Cars(1234, "asdf", 'asdfga', 'Erkak', 'asdfga', 1234, 'asdgfa','asdga')
lis.append(odam)
odam = Cars(1234, "asdf", 'asdfga', 'Erkak', 'asdfga', 1234, 'asdgfa','asdga')
lis.append(odam)

odam.metod1(lis)
