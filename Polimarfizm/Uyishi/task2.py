from random import randint

class Mylist(list):
    def rendom(self, n, min = -100, max = 100):
        lis = []
        for i in range(n):
            lis.append(randint(min,max))
        print(lis)

random = Mylist()
random.rendom(10, -5, 5)
