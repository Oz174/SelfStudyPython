"""
This python file is for the adapter design pattern
"""

class Target:
    """
    Target interface
    """
    def request(self) -> str:
        """
        Abstract method for the target interface
        """
        return "Target interface request"

class Adaptee:
    """
    Adaptee class
    """
    def specific_request(self) -> str:
        """
        Method for the adaptee class
        """
        return "Adaptee class request"[::-1]
    
class Adapter(Target):
    """
    Adapter class
    """
    def __init__(self, adaptee: Adaptee):
        self.adaptee = adaptee
        
    def request(self) -> str:
        """
        Method for the adapter class
        """
        return f"Adapter class request: {self.adaptee.specific_request()[::-1]}"
    
def client_code(target: Target) -> None:
    """
    Client code for the adapter class
    """
    print(target.request())


if __name__ == "__main__":
    print("Welcome to Adapter Pattern")
    print("This class aims to create an adapter class to convert the adaptee class request to the target class request")
    print("Creating the adaptee class")
    adaptee = Adaptee()
    print(adaptee.specific_request())
    print("Creating the adapter class")
    adapter = Adapter(adaptee)
    print("Client code for the adapter class")
    client_code(adapter)
    print("End of Adapter Pattern")
