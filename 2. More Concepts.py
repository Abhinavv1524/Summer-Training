a = 'Python'

print(len(a))

print(a[0])


str = 'Welcome to the 2nd class of Python'

print(str[::-1])

print(str[0:7])

print(str[-8:-3])

# check the string is palindrome or not
# name = input("Enter the name: ")
name = 'Nitin'
palindrome = name[::-1].capitalize()
if name == palindrome:
    print("The name is a palindrome")
else:
    print("The name is not a palindrome")

s = 'PyThOn ProGraMMing'
print(s.lower())
print(s.upper())
print(s.title())
print(s.capitalize())
print(s.swapcase())
print(s.casefold())
print(s.replace('ProGraMMing', 'Programming'))
print(s.split())
print(s.find('ProGraMMing'))
print(s.index('ProGraMMing'))

month = 'January'
sales = 1000

print(f"Sales in {month} were ${sales:,}")

print(f"Sales in {month} were ${sales:,.2f}")

x = 0
while x<20:
    x = x + 1
    if x == 10:
        continue
    elif x == 15:
        break
    print(x)

# write a program to check whether a number is prime or not
num = int(input("Enter a number: "))
is_prime = True
for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
        is_prime = False
        break

# write a prpgram to check a year is a leap year or not

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")

# write a program for armstrong number

num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if sum == num:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")

# another method for armstrong number with string conversion
num = int(input("Enter a number: "))
num_str = str(num)
sum = 0
for digit in num_str:
    sum += int(digit) ** len(num_str)

if sum == num:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")