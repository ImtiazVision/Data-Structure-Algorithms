### Abstract Base Classes

**Abstract Base Classes** : To be considered a duck-type instance of a class, abstract base classes describe a set of methods and attributes that a class must implement.

### Example : 

```
class Shape:  # Shape is a child class of ABC
    def area(self):
        pass

    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return (self.length * self.length)

    def perimeter(self):
        return (4 * self.length)


shape = Shape()
square = Square(4)
```
