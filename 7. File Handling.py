import os

cwd = os.getcwd()
print(f"Current working directory: {cwd}")

new_dir = "package"
if os.path.exists(new_dir):
    print(f"Directory '{new_dir}' already exists.")
else:
    os.mkdir(new_dir)

print("New directory created:", new_dir)

items = os.listdir('.')
print("Items in the current directory:")
for item in items:
    print(item)

print("\n")
# FILE OPERATIONS

file = open("sample.txt", "w")
file.write("Hello, this is a sample file.\n")
file.write("This file is created for demonstration purposes.\n")
file.close()
print("File 'sample.txt' created and written to.")
file = open("sample.txt", "r")
content = file.read()
print("Content of 'sample.txt':")
print(content)
file.close()

#readlines

file = open("sample.txt", "r")
content = file.readlines()
print("Content of 'sample.txt' using readlines():")
print(content)
file.close()

# seek function
file = open("sample.txt", "r")
file.seek(0)  # Move the cursor to the beginning of the file
content = file.read(10)  # Read the first 10 characters
print("First 10 characters of 'sample.txt':")
print(content)
file.close()

import pickle
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

with open('student.dat', 'wb') as file:
    student = Student("Abhinav", 22)
    pickle.dump(student, file)
    print("Student object serialized and saved to 'student.dat'.")

# adding more data to the same file
with open("student.dat", 'ab') as file:
    student = Student("Rishi", 23)
    pickle.dump(student, file)
    print("Student object serialized and saved to 'student.dat'.")
# reading the whole data from the file


with open("student.dat", 'rb') as file:
    while True:
        try:
            student = pickle.load(file)
            student.display()
        except EOFError:
            break  # End of file reached
print("All student objects deserialized and displayed.")

# try catch block
print("\n")
a = 10
b = 0
try:
    d = a/b
    print(d)
except ZeroDivisionError as e:
    print("Error: Division by zero is not allowed.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print("Division successful, result:", d)
finally:
    print("Execution of try-except block completed.")