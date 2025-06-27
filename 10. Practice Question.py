# Practice Question
# 1. Create 2. Display. 3. Raise Salary. 4. Exit
# on pressing 1 = enter name, age designation[Programmer, Manager, Tester] other designation should not allowed
# take the data from user
# Programmer salary = 25000, Manager = 30000, Tester = 20000
# after these three ask for continue yes or no if yes then ask name, age, designation again with no duplicates
# on pressing 2 = display name age salary designation
# on prerssing 3 . Raise salary, keep this as a abstract class
# on pressing 4. Exit the program and display thankyou message


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

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Designation: {self.designation}, Salary: {self.salary}")

    def raise_salary(self):
        pass
employees = {}

while True:
    print("\n1. Create\n2. Display\n3. Raise Salary\n4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        while True:
            name = input("Enter name: ")
            if name in employees:
                print("Employee already exists.")
                continue

            age = input("Enter age: ")
            designation = input("Enter designation (Programmer / Manager / Tester): ")

            if designation not in ['Programmer', 'Manager', 'Tester']:
                print("Invalid designation. Try again.")
                continue

            emp = Employee(name, age, designation)
            employees[name] = emp

            more = input("Do you want to add another employee? (yes/no): ")
            if more.lower() != 'yes':
                break

    elif choice == '2':
        if not employees:
            print("No employees to display.")
        else:
            for emp in employees.values():
                emp.display()

    elif choice == '3':
        pass

    elif choice == '4':
        print("Thank you for using the system.")
        break

    else:
        print("Invalid choice. Try again.")