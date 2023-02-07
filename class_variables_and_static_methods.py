
# Class variables ------------------------------------------------------------------------++
class Base:
    count = 0
    def __init__(self) -> None:
        Base.count += 1
    
    def __del__(self):
        print('object deleted.')
        Base.count -= 1
    
    @staticmethod
    def mymethod():
        print('hello world')

    
    
[Base() for _ in range(5)]
print()
print('Instances: ', Base.count)
print()
Base.mymethod()

x = Base(); print('Instances: ', Base.count)
del x;      print('Instances: ', Base.count)
# Class variables ------------------------------------------------------------------------++

