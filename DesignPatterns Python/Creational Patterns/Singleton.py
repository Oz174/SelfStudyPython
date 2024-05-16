class Singleton:
    _instance = None
    # the __new__ method is used to create a new instance of a class
    # it is called before the __init__ method
    # here , it checks if the instance is already created or not
    # if not, it creates a new instance and returns it
    # if it is already created, it returns the instance

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            # super() is used to call the __new__ method of the parent class
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def __init__(self, name):
        self.name = name


if __name__ == "__main__":
    print("Welcome to Singleton Pattern")
    print("This Class aims to create only one instance of the class and return the same instance whenever the class is called again.")
    a = Singleton('a')
    print("Created object A with name: ", a.name)
    b = Singleton('b')
    print("Created object B with name: ", b.name)

    print("Checking if both objects are same or not")
    print(a is b)
    print("Both objects are same")
    print("Changing the name of object A")
    print(a.name)
