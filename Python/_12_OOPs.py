class SimpleClass:
    x = 5                               # class variable/property/attribute

class initClass:                        # constructor, helps initilizing the values when object is created
    def __init__(self, x1, y):          #  __init__() function is called automatically every time the class is being used to create a new object.
        self.x = x1                     # use ObjectName.x to access the attribute/property, x1 scope is limited to assiging the value
        self.y = y

class strClass:
    def __init__(self, x, y):           # self is just a convention, it can be named anything but the first parameter
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"repr : (self.x = {self.x}, self.y = {self.y})"
    def __str__(mine):                  # we used mine in place of self, it can be named anything but the first parameter
        """Returns the string that the class returns, overriding the default string returned by the class"""
        return f"str : ({mine.x}, {mine.y})"  # This function is used to return the string that the class returns

class methodClass:
    def __init__(self, x = 2, y = 3):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def add(self):                      # this function/method is defined by us inside the class
        print(f"{self.x} + {self.y} = {self.x + self.y}")
        return self.x + self.y

class parentClass:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def add(self):
        print(f"{self.x} + {self.y} = {self.x + self.y}")

class childClass1(parentClass):
    pass

class childClass2(parentClass):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class childClass3(parentClass):
    def __init__(self, x, y, z):
        parentClass.__init__(self, x, y)# used to call the parent class constructor and initilize its values
        self.z = z

class childClass4(parentClass):
    def __init__(self, x, y, z):
        super().__init__(x, y)          # super() is used to call the parent class constructor and initilize its values
        self.z = z

    def add(self):                      # this function/method is defined by us inside the class
        print(f"{self.x} + {self.y} + {self.z} = {self.x + self.y + self.z}")

class polymorphicParentClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class polymorphicChildClass1(polymorphicParentClass):
    def operate(self):
        print(f"{self.x} + {self.y} = {self.x + self.y}")

class polymorphicChildClass2(polymorphicParentClass):
    def operate(self):
        print(f"{self.x} - {self.y} = {self.x - self.y}")

class polymorphicChildClass3(polymorphicParentClass):
    def operate(self):
        print(f"{self.x} * {self.y} = {self.x * self.y}")

# Iterator Classes

class iteratorClass1:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x

class iteratorClass2:
    def __iter__(self):
        self.z = 1
        return self
    
    def __next__(self):
        if self.z <= 10:
            x = self.z
            self.z += 1
            return x
        else:
            raise StopIteration



# -----------------------------------------------------------------------------------------------------------
# Objects
# -----------------------------------------------------------------------------------------------------------


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
object3                                 # returns str : (5, 6), since it was mentioned in the __str__ method
str(object3)                            # returns str : (5, 6), since it was mentioned in the __str__ method
repr(object3)                           # returns repr : (self.x = 5, self.y = 6), since it was mentioned in the __str__ method

repr(strClass)                          # returns <class '__main__.strClass'>
str(strClass)                           # returns <class '__main__.strClass'>
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



child1 = childClass1(7, 8)              # child1 is an instance/object of childClass1, which is a child of class parentClass
child1.x                                # returns 7, uses parentClass.x inherited by childClass

child2 = childClass2(-7, -8)            # __init__() inside childClass2 overrides the parent class inheritence
child2.x                                # returns -7, uses childClass2.x

child3 = childClass3(-9, -8, -7)        # parentClass.__init__() inside childClass3 initilizes the values through the parent class
child3.x                                # returns -9, uses parentClass.x
child3.z                                # returns -7, uses childClass3.z
child3.add()                            # using parentClass.add()

child4 = childClass4(-3, -6, -9)
child4.x                                # returns -3, uses parentClass.x
child4.z                                # returns -9, uses childClass3.z
child4.add()                            # using childClass4.add()



polyChild1 = polymorphicChildClass1(4, 7)
polyChild2 = polymorphicChildClass2(4, 7)
polyChild3 = polymorphicChildClass3(4, 7)

polyChild1.operate()                    # prints 4 + 7 = 11
polyChild2.operate()                    # prints 4 - 7 = -3
polyChild3.operate()                    # prints 4 * 7 = 28



iterableObj1 = iteratorClass1()
objIter1 = iter(iterableObj1)
next(objIter1)                          # returns 1
next(objIter1)                          # returns 2
next(objIter1)                          # returns 3

iterableObj2 = iteratorClass2()
objIter2 = iter(iterableObj2)
for x in objIter2:
    pass                                # x is iterated till it becomes 10
