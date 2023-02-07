

# ========================================================================================
# ========================================================================================

# wraps functionality around object creation
# addtional layer of protection

from abc import ABCMeta, abstractstaticmethod
class IAbstractClass(metaclass=ABCMeta):
    
    @abstractstaticmethod
    def class_method():
        """Implement in class."""

class CoreClass(IAbstractClass):
    def class_method(self):
        print('Core class executed...')

class ProxyClass(IAbstractClass):
    def __init__(self) -> None:
        super().__init__()
        self.core = CoreClass()
    def class_method(self):
        print('Proxy class executed...')
        self.core.class_method()
    
print('-----------------------')
c = CoreClass()
c.class_method()
print('-----------------------')
c = ProxyClass()
c.class_method()
print('-----------------------')


# ========================================================================================
# ========================================================================================
