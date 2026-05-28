#super = Function used in a child class to call methods from a parent class(superclass).
#        Allows you to extend the functionality of the inherited methods
#        (extending functionality = using both child and parent methods)

#        The child class is the subclass(Sub) while the parent class is the superclass(Super)
#        When a child class has it's own contstructor, it eliminates the need for the parent constructor
#        therefore, if we are interested in what is in the parent constructor, we need super()
#        when super() is used, everything in the parent constructor will be called
#        super() is "used" like the parent name itself

class Shape:
  def __init__(self, color, is_filled):
    self.color = color
    self.is_filled = is_filled

  def describe(self):
    print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
  def __init__(self, color, is_filled, radius):
    super().__init__(color, is_filled)
    self.radius = radius

  def describe(self): #method overiding
    super().describe() #extending functionality of the describe method from parent
    print(f"It is a circle with an area of {3.14 * self.radius *self.radius}cm^2")

class Square(Shape):
  def __init__(self, color, is_filled, width):
    super().__init__(color, is_filled)
    self.width = width
  
  def describe(self): 
    super().describe() 
    print(f"It is a square with an area of {self.width *self.width}cm^2")

class Triangle(Shape):
  def __init__(self, color, is_filled, width, height):
    super().__init__(color, is_filled)
    self.width = width
    self.height = height

  def describe(self): 
    super().describe() 
    print(f"It is a triangle with an area of {(self.width *self.height)/2}cm^2")

circle = Circle("red", True, 7)
square = Square("green", False, 10)
triangle = Triangle(color="black", is_filled = True, width=14, height=12)

print(circle.color)
print(f"{circle.radius}cm")
circle.describe()

print(square.color)
print(f"{square.width}cm")
square.describe()

print(triangle.color)
print(f"{triangle.width}cm")
print(f"{triangle.height}cm")
triangle.describe()