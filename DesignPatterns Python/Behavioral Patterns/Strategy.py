"""
This python file implements the strategy design pattern 
"""
from abc import ABC, abstractmethod

class CakeFactory(ABC):
    """
    Abstract class for the cake factory
    """
    @abstractmethod
    def get_ingredients(self):
        """
        Abstract method to get the cake
        """
        pass

    @abstractmethod
    def Make_Cake(self):
        """
        Abstract method to mix the ingredients
        """
        pass


class ChocolateCake(CakeFactory):
    """
    Concrete class for the chocolate cake
    """
    def get_ingredients(self):
        """
        Get the ingredients for the chocolate cake
        """
        return "Flour, Sugar, Cocoa, Baking Powder, Eggs, Milk, Oil, Vanilla Extract"

    def Make_Cake(self):
        """
        Mix the ingredients for the chocolate cake
        """
        return "Mix the ingredients for the chocolate cake"
    
class LemonCake(CakeFactory):
    """
    Concrete class for the lemon cake
    """
    def get_ingredients(self):
        """
        Get the ingredients for the lemon cake
        """
        return "Flour, Sugar, Lemon Zest, Baking Powder, Eggs, Milk, Oil, Lemon Juice"

    def Make_Cake(self):
        """
        Mix the ingredients for the lemon cake
        """
        return "Mix the ingredients for the lemon cake"
    
class StrawberryCake(CakeFactory):
    """
    Concrete class for the strawberry cake
    """
    def get_ingredients(self):
        """
        Get the ingredients for the strawberry cake
        """
        return "Flour, Sugar, Strawberries, Baking Powder, Eggs, Milk, Oil, Vanilla Extract"

    def Make_Cake(self):
        """
        Mix the ingredients for the strawberry cake
        """
        return "Mix the ingredients for the strawberry cake"
    
if __name__ == "__main__":
    print("Welcome to Strategy Pattern")
    print("This class aims to create different types of cakes using the factory design pattern")
    print("Choose a cake : \n 1- Chocolate Cake \n 2- Lemon Cake \n 3- Strawberry Cake")
    choice = input("Enter your choice : ")
    if choice == "1":
        cake = ChocolateCake()
    elif choice == "2":
        cake = LemonCake()
    elif choice == "3":
        cake = StrawberryCake()
    else:
        print("Invalid choice")
        exit()
    print("Ingredients for the cake : ", cake.get_ingredients())
    print("Making the cake : ", cake.Make_Cake())
    print("Enjoy your cake!")

