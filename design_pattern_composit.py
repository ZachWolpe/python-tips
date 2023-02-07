
# ========================================================================================
# ========================================================================================

# Composit: compile (sum)
# multiple classes that inherent from the parent class
# regions --> subregions


from abc import ABCMeta, abstractmethod, abstractstaticmethod

class IAbstractModule(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, nodes) -> None:
        """Implement in child class"""

    @abstractstaticmethod
    def print_data():
        """Implement in child class"""

class child_01(IAbstractModule):
    def __init__(self, nodes) -> None:
        self.nodes = nodes
        
    def print_data(self):
        print('child 01 has {} nodes.'.format(self.nodes))

class child_02(IAbstractModule):
    def __init__(self, nodes) -> None:
        self.nodes = nodes
        
    def print_data(self):
        print('child 02 has {} nodes.'.format(self.nodes))

class ParentClass(IAbstractModule):
    def __init__(self, nodes) -> None:
        # super().__init__(nodes)
        self.nodes      = nodes
        self.base_nodes = nodes
        self.children   = []
    
    def add_child(self, child):
        self.children.append(child)
        self.nodes += child.nodes
    
    def print_data(self):
        s = '\n'+'...'*10; print(s)
        print('Core nodes:  {}'.format(self.base_nodes))
        for chd in self.children:
            chd.print_data()
        print('Total nodes: {}'.format(self.nodes))
        s = '...'*10+'\n'; print(s)
c1 = child_01(21)
c2 = child_02(43)
p1 = ParentClass(6)
p1.add_child(c1)
p1.add_child(c2)
p1.print_data()


# ========================================================================================
# ========================================================================================
