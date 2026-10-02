# 3.1: Say Goodbye

name = "Joanne"

def say_goodbye(name):
# Prints "Goodbye, (name)"
    print("Goodbye," , name)

say_goodbye(name) # Input = Joanne, prints "Goodbye, Joanne"

# 3.2: Area of a Circle

def circlearea(radius):
    print(3.14 * (radius ** 2)) # Multiplies approximation of pi by radius squared. 

print(circlearea(1)) # Input = 1, prints 3.14.

# 4.1: Subtract, Multiply, and Divide

def subtract(a , b):
    return(a - b) # Subtracts first inputted value by second inputted value.

print(subtract(5, 3)) # Inputs 5 - 3, returns 2.


def multiply(a , b):
    return(a * b) # Multiplies both inputted numbers by eachother.

print(multiply(4 , 3)) # Inputs 4 * 3, returns 12.


def divide(a , b):
    return(a / b) # Divides first inputted value by second inputted value

print(divide(15 , 3)) # Inputs 15 / 3, returns 5.0


# 5.1: Conditionals:

reading = [69, 74, 55, 81, 77]

def temperatures(reading):
    return min(reading), max(reading)

print(temperatures(reading))

# 5.2: Check If Its The Weekend

days = [1, 2, 3, 4, 5, 6, 7]

def isweekend(days):
    for day in days:
        if days == 6 or days == 7:
                return True
        else:
                return False
    
print(isweekend(days))


# 5.3: Fuel Efficiency Calculator

def fuel_efficiency(miles, gallons):
    return(miles / gallons)

print(fuel_efficiency(100 , 50), "miles per gallon")

# 5.4: Secret Code

def encrypt(a):
    last = a % 10 # returns last digit
    rest = a // 10 # returns everything except last digit

    power = -1
    temp = a

    while temp > 0:
        power += 1
        temp = temp // 10
    
    encrypted = rest + (last * (10**power))
    return(encrypted)

# Plan:
# Need to take last number and move it to the front
# Last = returns last digit of number
# Rest = returns the number without the last digit
# Need to multiply last digit by the number of digits in the original number
# (Ex. 12345; last = 5, rest = 1234, need to multiply 5 by 1000 and add to 1234)
# Find power of number, multiply it by last, add to rest

print(encrypt(12345)) # Returns 51234
print(encrypt(23)) # Returns 32
print(encrypt(327)) # Returns 723

# 6.1: Oski Stole Your Power

def replacepower(x, y):
    result = 1 
    
    for i in range(y):
        result *= x
        i += 1

    return result

print(replacepower(2 , 3)) # Returns 8
print(replacepower(3 , 2)) # Returns 9 

# Plan: Multiply x by itself y times (2 * 2 * 2 = 2^3 = 8)
# Step 1: For every value until y, multiply x by itself (start at 0 end at y?)  

# 6.2.1: For Loops

numbers = [5, 7, 2, 12, 9]

def forminmax(numbers):
    minnum = numbers[0]
    maxnum = numbers[0]

    for num in numbers:
        if minnum > num:
            minnum = num

        if maxnum < num:
            maxnum = num
    
    return minnum, maxnum

print(forminmax(numbers))

# Plan: iterate through the list and return the lowest value
# Step 1: For num in numbers iterates through entire list and performs a function for every iteration
# Step 2: Check if every number is less than/greater than first number

# 6.2.2: While Loops

def whileminmax(numbers):
    minnum2 = numbers[0]
    maxnum2 = numbers[0]

    while True:
        for num in numbers:
            if minnum2 >  num:
                minnum2 = num
            if maxnum2 < num:
                maxnum2 = num
        break
    return minnum2, maxnum2


print(whileminmax(numbers))

# Plan: cry


# 6.3: Calculate Sum

def calculatesum(input):
    sum = 0

    while input != 0:
        sum = sum + (input % 10)
        input = input // 10

    return sum
    
print(calculatesum(2468)) # Returns 2 + 4 + 6 + 8 = 20
print(calculatesum(1450)) # Returns 1 + 4 + 5 = 10

# Plan: integer // 10 returns everything except the last number, so can store last number in a variable and replace integer with integer // 10 
# integer % 10 returns the last number, so can add to sum

# Favorite Function (aka the one that took me the longest): 5.4: Secret Code

def encrypt(a):
    last = a % 10 # returns last digit
    rest = a // 10 # returns everything except last digit

    power = -1
    temp = a

    while temp > 0:
        power += 1
        temp = temp // 10
    
    encrypted = rest + (last * (10**power))
    return(encrypted)

# Plan:
# Need to take last number and move it to the front
# Last = returns last digit of number
# Rest = returns the number without the last digit
# Need to multiply last digit by the number of digits in the original number
# (Ex. 12345; last = 5, rest = 1234, need to multiply 5 by 1000 and add to 1234)
# Find power of number, multiply it by last, add to rest

print(encrypt(12345)) # Returns 51234
print(encrypt(23)) # Returns 32
print(encrypt(327)) # Returns 732








    