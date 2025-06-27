class mobile:
    def __init__(self):
        self.brand = "Samsung"
        self.model = "Galaxy S21"
        self.price = '₹80000'

    def display(self):
        print("Brand", self.brand, "Model", self.model, "Price", self.price)


Samsung = mobile()
Samsung.display()
print("\n")
class addition():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        print("the sum of 2 numbers are", self.num1 + self.num2)

add = addition(5,6)
add.addition()
print("\n")
class mobile:
    def __init__(self):
        self.brand = "Samsung"
        self.model = "Galaxy S21"
        self.price = '₹80000'

    def display(self, calling):
        calling = calling
        print("Brand", self.brand, "Model", self.model, "Price", self.price)
        print("Calling", calling)

Samsung = mobile()
Samsung.display("Hello, this is a test call!")

print("\n")
class Addition:
    def __init__(self, num1, num2):
        self.__num1 = num1
        self.__num2 = num2

    def set_num2(self, num2):
        self.__num2 = num2  # update private variable

    def get_num2(self):
        return self.__num2

    def addition(self):
        print("The sum of 2 numbers is", self.__num1 + self.__num2)

# Create object
add = Addition(5, 6)

# Access using getter
print("num2 is:", add.get_num2())

# Attempting to access private attributes directly → will raise an error
# print(add.__num1)     # Error

# Use the method
add.addition()

class army:
    def __init__(self):
        self.name = "Abhinav"
        self.gn = self.Gun()

    def show(self):
        print("Name", self.name)

    class Gun:
        def __init__(self):
            self.name = "AK47"
            self.capacity = "75 Rounds"
            self.length = "34.4 In"

        def disp(self):
            print("Gun name", self.name)
            print("Capacity", self.capacity)
            print("Length", self.length)

print("\n")
# Create an object of the outer class
soldier = army()
soldier.show()
# Create an object of the inner class
gun = soldier.gn
gun.disp()

# inheritance
print("\n")
class Father:
    def __init__(self):
        self.name = "John"
        self.age = 50
    def show(self):
        print("Father's Name:", self.name)
        print("Father's Age:", self.age)

class Son(Father):
    def __init__(self):
        super().__init__()
        print("Father Name from Son class:", self.name)
s = Son()
s.show()
print(s.name)

## multi level inheritance
print("\n")
class Grandfather:
    def __init__(self):
        print("Grandfather constructor")
    def showGF(self):
        print("Grandfather's Method",)

class Father(Grandfather):
    def __init__(self):
        # super().__init__()
        print("Father constructor")
    def showF(self):
        print("Father's Method",)

class Son(Father):
    def __init__(self):
        # super().__init__()
        print("Son constructor")
    def showS(self):
        print("Son's Method",)

S = Son()
S.showS()
S.showF()
S.showGF()

## Multiple Inheritance
print("\n")
class Father:
    def __init__(self):
        print("Father constructor")
    def showF(self):
        print("Father's Method")

class Mother:
    def __init__(self):
        print("Mother constructor")
    def showM(self):
        print("Mother's Method")

class Son(Father, Mother):
    def __init__(self):
        print("Son constructor")
    def showS(self):
        print("Son's Method")

S = Son()
S.showS()
S.showM()
S.showF()