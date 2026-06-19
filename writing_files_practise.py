file_path = "C:/Users/essya/Desktop/test.txt"
print(file_path)
data = "The world and it's elements are all God's doings"

with open(file_path, 'w') as file:
  file.write(data)