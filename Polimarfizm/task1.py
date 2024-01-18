class Mylist(list):
    def save(self, element):
        n=0
        while  n<len(self):
            if element !=  self[n] :
                self.remove(self[n])
                n -= 1
            n += 1
        return self

lis = Mylist([1,2,3,1,4,5,6,1,1,3,4,5,6])
lis.save(1)
print(lis)
