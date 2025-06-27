class Cal():
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b

cal = Cal()
print(cal.add(5, 3))
print(cal.subtract(10, 4))
print(cal.multiply(2, 6))
print(cal.divide(8, 2))

#  create display raise salary exit
#
# 1. enter name
# 2. enter age

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}")

    def raise_salary(self, amount):
        self.salary += amount
        print(f"New salary for {self.name} is: {self.salary}")

    def exit(self):
        print(f"{self.name} has exited the system.")


emp1 = Employee("Abhinav", 24, 15000)
emp1.display()
emp1.raise_salary(50000)
emp1.display()