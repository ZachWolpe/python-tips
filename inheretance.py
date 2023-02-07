

# Inheritance ----------------------------------------------------------------------------++
class Car:
    def __init__(self, type, age) -> None:
        self.type = type
        self.age  = age

class Ferrari(Car):
    def __init__(self, type, age, speed) -> None:
        super(Ferrari, self).__init__(type, age)
        self.speed = speed
    
    
    # override
    def __str__(self) -> str:
        text = super().__str__()
        text += 'Ferrari!'
        return text

print(Ferrari('sport','3','3.21'))
# Inheritance ----------------------------------------------------------------------------++
