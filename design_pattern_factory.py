

# ========================================================================================
# ========================================================================================

# increase modularity -> separations of concerns
from abc import ABCMeta, abstractstaticmethod

class IAbstractClass(metaclass=ABCMeta):
    
    @abstractstaticmethod
    def print_class_type():
        """Interface Method"""
        pass


class subclass_01(IAbstractClass):
    def __init__(self) -> None:
        super().__init__()
        
    def print_class_type(self):
        print('Class 01')


class subclass_02(IAbstractClass):
    def __init__(self) -> None:
        super().__init__()
    
    def print_class_type(self):
        print('Class 02')


class Factory:

    @staticmethod
    def build_subclass(class_type):
        if class_type == 'aaa':
            return subclass_01()
        return subclass_02()


if __name__ == '__main__':
    choice = input('Type of class?\n')
    person = Factory.build_subclass(choice)
    person.print_class_type()
# ========================================================================================
# ========================================================================================
