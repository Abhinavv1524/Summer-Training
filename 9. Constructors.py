class Test(object):
    def __init__(self):
        print("Test constructor")
    def m1(self):
        print("Hello world")

x = Test()
x.m1()

class Atm(object):
    def __init__(self):
        print("ATM Database connected")

    def deposit(self, amount):
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        print(f"Withdrawn: {amount}")

    def mini_statement(self):
        print("Mini Statement: Balance is $1000")

atm = Atm()
atm.deposit(500)
atm.withdraw(200)
atm.mini_statement()

class Father:
    def show(self):
        print("Father's Method")
class Son(Father):
    def disp(self):
        print("Son's Method")

s = Son()
s.show()
s.disp()

class grandfather:
    def showGF(self):
        print("Grandfather's Method")
class father(grandfather):
    def showF(self):
        print("Father's Method")

class son(father):
    def showS(self):
        print("Son's Method")

s = son()
s.showS()
s.showF()
s.showGF()

print("\n")

lst = [1,2,3,4,"Python Programming", 5.6, True]

for item in lst:
    print(item)
lst[0] = 10
print(lst)
lst.remove(10)
lst.insert(0,1)
print(lst)

# set
s = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(s)
s.add(10)
print(s)
s.remove(10)
print(s)
for item in s:
    print(item, end=' ')

# dictionary
dict = {"Name": "Abhinav", "Age": 24, "Skills" : {"Data Science" : "Python", "Web Development": "Django"}}
print("\nDictionary:")
for key, value in dict.items():
    print(f"{key}: {value}")

# Accessing nested dictionary
print("Skills:")
for skill, tech in dict["Skills"].items():
    print(f"{skill}: {tech}")

#modifying dictionary
dict["Age"] = 25
print("Modified Age:", dict["Age"])
# Adding a new key-value pair
dict["Location"] = "India"
print("After adding Location:", dict)
# Removing a key-value pair
del dict["Location"]
print("After removing Location:", dict)
# Checking if a key exists
if "Name" in dict:
    print("Name exists in the dictionary:", dict["Name"])


# Practice Question
# 1. Create 2. Display. 3. Raise Salary. 4. Exit
# 1 = enter name, age designation[Programmer, Manager, Tester] other should not allow
# Programmer salary = 25000, Manager = 30000, Tester = 20000
# after these three ask for continue yes or no if yes then ask name, age, designation again with no duplicates
# 2 = display name age salary designation
# 3 . Raise salary
# 4. Exit the program and display thankyou message