"""
This python file is for the facade design pattern
"""

class SubsystemA:
    """
    Subsystem A class
    """
    def operation1(self) -> str:
        """
        Operation 1 for the subsystem A
        """
        return "Subsystem A, Operation 1 \n"
    
    def operation2(self) -> str:
        """
        Operation 2 for the subsystem A
        """
        return "Subsystem A, Operation 2 \n"
    
class SubsystemB:
    """
    Subsystem B class
    """
    def operation1(self) -> str:
        """
        Operation 1 for the subsystem B
        """
        return "Subsystem B, Operation 1 \n"
    
    def operation2(self) -> str:
        """
        Operation 2 for the subsystem B
        """
        return "Subsystem B, Operation 2\n "
    
class Facade:
    """
    Facade class
    """
    def __init__(self, subsystemA: SubsystemA, subsystemB: SubsystemB):
        self.subsystemA = subsystemA
        self.subsystemB = subsystemB
        
    def operation(self) -> str:
        """
        Operation for the facade
        """
        result = "Facade initializes subsystems:\n"
        result += self.subsystemA.operation1()
        result += self.subsystemB.operation1()
        result += "Facade orders subsystems to perform the action:\n"
        result += self.subsystemA.operation2()
        result += self.subsystemB.operation2()
        return result
    
def client_code(facade: Facade) -> None:
    """
    Client code for the facade
    """
    print(facade.operation())
    
if __name__ == "__main__":

    print("Welcome to Facade Pattern")
    print("This class aims to create a facade class to simplify the complex subsystems")
    print("Creating the subsystems")
    subsystemA = SubsystemA()
    subsystemB = SubsystemB()
    print("Creating the facade class")
    facade = Facade(subsystemA, subsystemB)
    print("Client code for the facade class")
    client_code(facade)
    print("End of Facade Pattern")
