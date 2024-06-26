"""
This python file is for the decorator design pattern
"""

from abc import ABC, abstractmethod

class Component(ABC):
    """
    Abstract class for the component
    """
    @abstractmethod
    def operation(self) -> str:
        """
        Abstract method for the operation
        """
        pass

class ConcreteComponent(Component):
    """
    Concrete class for the component
    """
    def operation(self) -> str:
        """
        Operation for the concrete component
        """
        return "ConcreteComponent"
    
class Decorator(Component):
    """
    Abstract class for the decorator
    """
    def __init__(self, component: Component):
        self.component = component
        
    @abstractmethod
    def operation(self) -> str:
        """
        Abstract method for the operation
        """
        pass

class ConcreteDecoratorA(Decorator):
    """
    Concrete class for the decorator A
    """
    def operation(self) -> str:
        """
        Operation for the concrete decorator A
        """
        return f"ConcreteDecoratorA({self.component.operation()})"
    
class ConcreteDecoratorB(Decorator):
    """
    Concrete class for the decorator B
    """
    def operation(self) -> str:
        """
        Operation for the concrete decorator B
        """
        return f"ConcreteDecoratorB({self.component.operation()})"
    
def client_code(component: Component) -> None:
    """
    Client code for the decorator pattern
    """
    print(f"RESULT: {component.operation()}")

if __name__ == "__main__":
    print("Welcome to Decorator Pattern")
    print("This class aims to create a decorator class to add functionality to the component class")
    print("Creating the concrete component")
    component = ConcreteComponent()
    print("Client code for the decorator pattern")
    print("Client: I've got a simple component:")
    client_code(component)
    print("\n")
    decorator1 = ConcreteDecoratorA(component)
    decorator2 = ConcreteDecoratorB(decorator1)
    print("Client: Now I've got a decorated component:")
    client_code(decorator2)
    print("End of Decorator Pattern")