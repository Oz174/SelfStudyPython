class Inventory:
    def __init__(self):
        self.observers = []
        self._product = None
        self._quantity = 0

    def attach(self, observer):
        self.observers.append(observer)

    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, value):
        self._product = value
        self._update_observers()

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
        self._update_observers()

    def _update_observers(self):
        for observer in self.observers:
            observer()


class ConsoleObserver:
    def __init__(self, inventory):
        self.inventory = inventory

    def __call__(self):
        if self.inventory.quantity > 4:
            print(f"{self.inventory.product} has {self.inventory.quantity}, overload warning!")
        print(self.inventory.product)
        print(self.inventory.quantity)


if __name__ == "__main__":
    # Create an inventory
    inventory = Inventory()

    # Create observers
    console_observer1 = ConsoleObserver(inventory)
    console_observer2 = ConsoleObserver(inventory)

    # Attach observers to the inventory
    inventory.attach(console_observer1)
    inventory.attach(console_observer2)

    # Update the inventory
    inventory.product = "Apples"
    inventory.quantity = 10