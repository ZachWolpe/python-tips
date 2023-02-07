

# encapsulation ------------------------------------------------------------------------------++
class Person:
    def __init__(self, age) -> None:
        self.__age = age

    @property
    def Age(self):
        return self.__age
    
    @Age.setter
    def Age(self, value):
        if value <= 0:
            return
        else:
            self.__age = value


p1 = Person(20)
print()
print(p1.Age)

p1.Age = -2342
print(p1.Age)

p1.Age = 2342
print(p1.Age)
print()
# encapsulation ------------------------------------------------------------------------------++
