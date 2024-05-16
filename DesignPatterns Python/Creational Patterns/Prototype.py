from typing import Optional


class Shape:
    def __init__(self, shape: Optional['Shape']):
        if shape is not None:
            self.x = shape.x
            self.y = shape.y
            self.color = shape.color
        else:
            self.x = 0
            self.y = 0
            self.color = 'white'

    def clone(self):
        pass


class Rectangle(Shape):
    def __init__(self, rectangle: Optional['Rectangle']):
        super().__init__(rectangle)
        if rectangle is not None:
            self.width = rectangle.width
            self.height = rectangle.height
        else:
            self.width = 0
            self.height = 0

    def clone(self):
        return Rectangle(self)


class Circle(Shape):
    def __init__(self, circle: Optional['Circle']):
        super().__init__(circle)
        if circle is not None:
            self.radius = circle.radius
        else:
            self.radius = 0

    def clone(self):
        return Circle(self)


if __name__ == "__main__":
    # test Prototype pattern
    shapes = []
    circle = Circle(None)
    circle.x = 10
    circle.y = 10
    circle.color = 'red'
    circle.radius = 20
    shapes.append(circle.clone())
    rectangle = Rectangle(None)
    rectangle.width = 10
    rectangle.height = 20
    rectangle.color = 'blue'
    shapes.append(rectangle.clone())
    for shape in shapes:
        print(shape.color)
        print(shape.x)
        print(shape.y)
        if isinstance(shape, Circle):
            print(shape.radius)
        else:
            print(shape.width)
            print(shape.height)
        print('')
