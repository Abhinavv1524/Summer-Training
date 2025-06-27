def myfirstfunction(x,y):
    sum = x+y
    return sum

print(myfirstfunction(5, 10))

def second(y,x = 5):
    sum = x + y
    return sum

print(second(10))

def display():
    def show():
        return "Hello from the inner function!"
    return show() + " and outer function!"

print(display())

def add_numbers(x,y):
    z = x + y
    print("Addition", z)

add_numbers(3, 5)

def func(*args):
    print("Arguments:", args)
    for arg in args:
        print(arg)

func(1, 2, 3, 4, 5)

def func_with_kwargs(**kwargs):
    print("Keyword Arguments:", kwargs)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

func_with_kwargs(name="Alice", age=30, city="New York")

def trial(*args, **kwargs):
    print("Positional Arguments:", args)
    print("Keyword Arguments:", kwargs)

trial(1, 2, 3, name="Bob", age=25)


def plus(a, b):
    return a + b
def minus(a, b):
    return a - b

def func3(a,b):
    return plus(a, b) / minus(a, b)

print(func3(10, 5))

#recursion

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print("Factorial of 5 is:", factorial(5))

# fibonacci series using recursion
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = fibonacci(n - 1)
        fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series

print("Fibonacci series up to 10 terms:", fibonacci(10))


# lambda functions
show = lambda x: x + 10
print("Result of lambda function:", show(5))

def armstrongnum(num):
    strnum = str(num)
    power = len(strnum)
    sum = 0
    for digit in strnum:
        sum += int(digit) ** power

    if sum == num:
        return f'{num} is an Armstrong number'
    else:
        return f'{num} is not an Armstrong number'

print(armstrongnum(153))