class SimpleClass:
    x = 5                               # class variable/property/attribute

class initClass:
    def __init__(self, x, y):           # constructor, helps initilizing the values when object is created
        self.x = x
        self.y = y

class strClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x}, {self.y})"

class methodClass:
    def __init__(self, x = 2, y = 3):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def add(self):
        print(f"{self.x} + {self.y} = {self.x + self.y}")
        return self.x + self.y



SimpleClass.x                           # returns 5, the value of x in SimpleClass

object1 = SimpleClass()                 # object1 is an instance/object of SimpleClass
object1                                 # returns <__main__.initClass object at <respective Memory Address>>
object1.x                               # returns 5
object1.x = 6                           # updates the value of x within the instance object1 to 6
object1.x                               # returns 6

SimpleClass.x                           # returns 5
SimpleClass                             # returns <class '__main__.SimpleClass'>



object2 = initClass(5, 6)               # object2 is an instance/object of initClass
object2                                 # returns <__main__.initClass object at <respective Memory Address>>
object2.x                               # returns 5
object2.y                               # returns 6
object2.x = 7                           # updates the value of x within the instance object2 to 7
object2
initClass                               # returns <class '__main__.initClass'>



object3 = strClass(5, 6)                # object3 is an instance/object of strClass
object3                                 # returns (5, 6), since it was mentioned in the __str__ method

strClass                                # returns <class '__main__.strClass'>



object4 = methodClass(5, 6)             # object4 is an instance/object of methodClass
object4                                 # returns (5, 6), since it was mentioned in the __str__ method
object4.x                               # returns 5
object4.y                               # returns 6
object4.x = 7                           # updates the value of x within the instance object4 to 7
object4.add()                           # prints 7 + 6 = 13, returns 13
print(object4.add())                    # prints 7 + 6 = 13, then 13 in the next line

object5 = methodClass()                 # object5 is an instance/object of methodClass
object5                                 # returns (2, 3), since it was mentioned in the __init__ method
object5.add()                           # prints 2 + 3 = 5, returns 5
object5.__init__(0, 1)                  # updates the value of x within the instance object x = 0, y = 1
object5.__str__()                       # returns (0, 1), since it was mentioned in the __str__ method and previously updated through __init__ method
object5                                 # returns (0, 1), since it was mentioned in the __str__ method

del object5.x                           # deletes the value of x within the instance object5

del object5                             # deletes the instance object5

methodClass                             # returns <class '__main__.methodClass'>
