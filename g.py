class Dog:
    mammal=True
    def __init__(self,nickname,breed,age):
        self.breed =breed
        self.age=age
        self.nickname=nickname

chapi = Dog('Chapi','Haski',12)
print(chapi.nickname)
print(chapi.breed)
print(chapi.age)
