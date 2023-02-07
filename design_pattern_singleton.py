
# ============================================================
# ============================================================

# Class --> one single instance (vs as many can fit into memory)

from abc import ABCMeta, abstractclassmethod

# ABSTRACT CLASSES ===========================================
from abc import ABCMeta, abstractstaticmethod

class IAbstractClass(metaclass=ABCMeta):

    @abstractstaticmethod
    def method_01():
        pass

class child_class(IAbstractClass):

    @staticmethod
    def method_01():
        print('required method implemented!')


# child_class.method_01()
# ABSTRACT CLASSES ===========================================


# ============================================================
# ============================================================

# Class --> one single instance (vs as many can fit into memory)
from abc import ABCMeta, abstractstaticmethod

class IAbstractClass(metaclass=ABCMeta):

    @abstractstaticmethod
    def print_data():
        pass

class Singleton(IAbstractClass):
    __instance = None

    def __init__(self) -> None:
        if Singleton.__instance is not None:
            raise Exception('Singleton cannot be instantiated more than once.')
        super().__init__()
        Singleton.__instance = self

    @staticmethod
    def get_instance():
        if Singleton.__instance is not None:
            return Singleton.__instance
        return 'No instance of Singleton.'

    @staticmethod
    def print_data():
        print(f'{Singleton.__instance}')




# Singleton.get_instance()
s1 = Singleton()
s1.print_data()
print(Singleton.get_instance())
# ============================================================
# ============================================================


