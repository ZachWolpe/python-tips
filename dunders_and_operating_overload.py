
# dunder ----------------------------------------------------------------------++

class Example:
    def __init__(self) -> None:
        pass

    def __del__(self):
        pass

    def __str__(self) -> str:
            txt = super().__str__()
            txt += ' - added to text...'
            return txt

    def __call__(self, *args, **kwds):
        print(f'\n{self.__class__.__name__} was called!')

ex = Example()
print()
print(ex)
ex()
print()
# dunder ----------------------------------------------------------------------++

# Operator Overloading --------------------------------------------------------++
class Vector:
    def __init__(self,x,y) -> None:
        self.x, self.y = x, y
    
    def __del__(self):
        pass

    def __add__(self, other):
        return Vector(self.x+other.x, self.y+other.y)

    def __str__(self) -> str:
        return '    x:{}, y:{}'.format(self.x, self.y)

v1 = Vector(1,2)
v2 = Vector(5,4)
v3 = v1 + v2
print(v1)
print(v2)
print(v3)
print()
# Operator Overloading --------------------------------------------------------++



