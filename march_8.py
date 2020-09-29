class Person:
    def __init__(self, name, contribution):
        self.name=name
        self.contribution=contribution
    def getinfo(self):
        return self.name, self.contribution

number_of_members=int(input("Enter numbers of members:"))
#dc={str(i):Person(str(input("Enter name:")), int(input("Enter contribution:"))) for i in range(1, number_of_members+1)}
#print(dc)
for i in range(1, number_of_members+1):
    i=Person(str(input("Enter name:")), int(input("Enter contribution:")))
    print(i.getinfo())
    print(i.name)
