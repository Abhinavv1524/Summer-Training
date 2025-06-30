# Practice Question
# 1. Create 2. Display. 3. Raise Salary. 4. Exit
# on pressing 1 = enter name, age designation[Programmer, Manager, Tester] other designation should not allowed
# take the data from user
# Programmer salary = 25000, Manager = 30000, Tester = 20000
# after these three ask for continue yes or no if yes then ask name, age, designation again with no duplicates
# on pressing 2 = display name age salary designation
# on prerssing 3 . Raise salary, keep this as a abstract class
# on pressing 4. Exit the program and display thankyou message
# Now i want this data to be stored in a file system using file handling dont use abstract class

import json
import os
class Employee:
    def __init__(self, name, age, designation):
        self.name = name
        self.age = age
        self.designation = designation
        self.salary = self.set_salary()

    def set_salary(self):
        if self.designation == "Programmer":
            return 25000
        elif self.designation == "Manager":
            return 30000
        elif self.designation == "Tester":
            return 20000
        else:
            return 0

    def raise_salary(self, amount):
        self.salary += amount
    
def to_dict(self):
    return {
        "name": self.name,
        "age": self.age,
        "designation": self.designation,
        "salary": self.salary
    }
def from_dict(data):
    return Employee(data['name'], data['age'], data['designation'])
def save_employees(employees, filename='employees.json'):
    with open(filename, 'w') as file:
        json.dump([emp.to_dict() for emp in employees], file, indent=4)
def load_employees(filename='employees.json'):
    if not os.path.exists(filename):
        return []
    with open(filename
, 'r') as file:
        data = json.load(file)
        return [from_dict(emp) for emp in data]
def display_employees(employees):
    if not employees:
        print("No employees to display.")
        return
    print(f"{'Name':<20} {'Age':<5} {'Designation':<15} {'Salary':<10}")
    for emp in employees:
        print(f"{emp.name:<20} {emp.age:<5} {emp.designation:<15} {emp.salary:<10}")
def main():
    employees = load_employees()
    while True:
        print("\n1. Create Employee")
        print("2. Display Employees")
        print("3. Raise Salary")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter name: ")
            age = input("Enter age: ")
            designation = input("Enter designation (Programmer, Manager, Tester): ")
            if designation not in ["Programmer", "Manager", "Tester"]:
                print("Invalid designation. Please try again.")
                continue
            if any(emp.name == name for emp in employees):
                print("Employee with this name already exists.")
                continue
            employee = Employee(name, age, designation)
            employees.append(employee)
            save_employees(employees)
            print(f"Employee {name} added successfully.")
        
        elif choice == '2':
            display_employees(employees)
        
        elif choice == '3':
            name = input("Enter the name of the employee to raise salary: ")
            amount = float(input("Enter the amount to raise salary by: "))
            for emp in employees:
                if emp.name == name:
                    emp.raise_salary(amount)
                    save_employees(employees)
                    print(f"Salary of {name} raised by {amount}. New salary is {emp.salary}.")
                    break
            else:
                print(f"No employee found with name {name}.")
        
        elif choice == '4':
            print("Thank you for using the employee management system!")
            break
        
        else:
            print("Invalid choice. Please try again.")



