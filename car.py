class Car:
  #def __init__(self): #constructor method, self is a must
  #__init__ is used to initialize an object with values when it is created
  #self means object is being created right now
  #after self, other variables can be written
  def __init__(self, model, year, color, for_sale): #attributes
    self.model = model
    self.year = year
    self.color = color
    self.for_sale = for_sale

  def drive(self): #methods
    print(f"You drive the {self.color} {self.model}")
  
  def stop(self):
    print(f"You stop the {self.color} {self.model}")
  
  def describe(self):
    print(f"{self.year} {self.color} {self.model}")