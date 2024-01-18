from random import randint

class Mylist(list):
    def rando(self, n, min = -100, max = 100):
        lis = []
        for i in range(n):
            lis.append(randint(min,max))
        print(lis)

random = Mylist()
random.rando(10, -5, 5)
