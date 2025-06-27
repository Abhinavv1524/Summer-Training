print('Hello World')

x = "Python"
y = "Programming"

print(x,y)

print(x+y)

print(x + " " + y)
for i in x :
    print("hi", end='')

print(" ")

print("hi" * 5)

for i in range(1,5):
    print('*' * i)

# base = float(input("Enter base: "))
# height = float(input("Enter height: "))
#
# area = 0.5 * base * height
# print("Area of triangle is: ", area)

a = 4
b = 5
a, b = b, a
print("a =", a)
print("b =", b)

# centimeters = float(input("Enter length in centimeters: "))
# feet = centimeters / 30.48
# inches = (centimeters % 30.48) / 2.54
# print(f"{centimeters} centimeters is {int(feet)} feet and {inches:.2f} inches.")

fibbonacci = [0, 1]
for i in range(2, 20):
    next_value = fibbonacci[i - 1] + fibbonacci[i - 2]
    fibbonacci.append(next_value)

print("Fibonacci series:", fibbonacci)

factorial = 1
for i in range(1, 6):
    factorial *= i

print("Factorial of 5 is:", factorial)

table = int(input("Enter a number to print its multiplication table: "))
for i in range(1, 11):
    print(f"{table} x {i} = {table * i}")
    