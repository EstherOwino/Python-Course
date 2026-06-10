#Magic methods = Dunder methods (double underscore) __init__, __str__, __eq__
#                They are automatically called by many of Python's built-in operations.
#                They allow developers to define or customize the behaviour of objects

class Book:
  def __init__(self, title, author, num_pages):
    self.title = title
    self.author = author
    self.num_pages = num_pages

  def __str__(self):
    #when I print print(book1), it returns a memory address
    #instead of having that, we can customize that behaviour
    return f"'{self.title}' {self.author}"
  
  def __eq__(self, other):
    # when I print(book1 == book2) it returns false
    # this is because memory addresses are different
    # that can be customised here
    return self.title == other.title and self.author == other.author
  
  def __lt__(self, other): #lt = less than
    return self.num_pages < other.num_pages
  
  def __gt__(self, other): #gt = greater than
    return self.num_pages > other.num_pages
  
  def __add__(self, other): #adds
    return f"{self.num_pages + other.num_pages} pages"
  
  def __contains__(self, keyword):#pass in parameter keyword for what we are searching for
    return keyword in self.title or keyword in self.author
  
  def __getitem__(self, key):
    if key == "title":
      return self.title
    elif key == "author":
      return self.author
    elif key == "num_pages":
      return self.num_pages
    else:
      return f"Key {key} was not found"

book1 = Book("Beyond the horizon", "Brian Okari", 220)
book2 = Book("Beyond the horizon", "Brian Okari", 220)
book3 = Book("You are the change, arise and make a difference", "Erick", 300)

print(book3)
print(book1 == book2)#memory addresses are different hence returns false, this can be customised in __eq__
print(book1 > book2)#uses __gt__
print(book2 < book3)#generates an error, can ne customised using __lt__ which means less than
print(book2 + book3)#uses __add__
print("change" in book3)#uses __contains__...this is for getting keyword
print(book1["num_pages"])#this is for getting key...uses __getitem__ method
print(book2["title"])
print(book3["author"])
print(book3["None"])
print(book3[""])