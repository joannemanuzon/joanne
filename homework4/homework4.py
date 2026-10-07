# Homework 4

# 3.1 List Operations

foods = ["cookie dough" , "cpk mac n cheese" , "margherita pizza" , "buldak" , "summer pasta"]

print(foods[1])

print(foods[-1])

foods.append("diet coke")

foods.insert(0, "apple") # Error 1: switched index and item placement, fixed it by putting index first then item after

foods.remove("margherita pizza") # Error 2: used index instead of string, fixed it by using string instead

print(len(foods))

for food in foods:
    print(food[0].upper() + food[1:]) # Prints first letter as uppercase + the rest of the word starting at index 1
# Error 3: printed everything as uppercase, fixed it by using food[0].upper() to only print the first letter as uppercase

foods2 = []

foods2.append(foods[::len(foods)-1]) # Slices through the entire foods list at a step of the length of the list

print(foods2)

if "potato" in foods:
    print("A potato!")
else:
    print("No potato!")

# 3.2 Slicing and Striding

numbers = []

i = 0

for i in range(21):
    numbers.append(i)
    i += 1
print(numbers)


def get_first_15(numbers):
    fifteennumbs = []
    
    for numb in numbers:
        if numb <= 15:
            fifteennumbs.append(numb)
    return(fifteennumbs)
step1 = get_first_15(numbers)
print(step1)


def get_every_5th(step1):
    return(step1[0:21:5])
step2 = get_every_5th(step1)
print(step2)


def reverse_and_stride(step2):
    reversed = step2[::-1]
    bythree = reversed[::3]

    return(bythree)
print(reverse_and_stride(step2))

# 3.3.1 Nested Lists Operations

numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(numbers[2])

numbers.append([10, 11, 12])

def sum_nested(numbers):
    sum = 0
    for row in numbers:
        for num in row:
            sum += num
    return(sum)

print(sum_nested(numbers))

# 3.4 Create a 5x5 List

def createlist():
    fxf = []
    count = 0

    for i in range(5):
        row = []
        for x in range(5):
            row.append(count)
            count += 1
        fxf.append(row)
    return(fxf)

fxflist = createlist()

def multiplesof3(fxflist):
    threefxf = []
    
    for row in fxflist:
        threefxfrow = []
        for num in row:
            if num % 3 == 0:
                threefxf.append("?")
            else:
                threefxfrow.append(num)
        threefxf.append(threefxfrow)

    return(threefxf)

three = multiplesof3(fxflist)
print(three)

def sumofthree(three):
    sum = 0

    for row in three:
        for num in row:
            if num != "?":
                sum += num
    return(sum)

print(sumofthree(three))

# 3.4 Dictionaries

ages = {
    "Katie": 30,
    "Mariam": 42,
    "Safia": 25,
    "Mira": 48
}

print(ages["Katie"])

ages.update({"Mira": 100})

ages.update({"Milana" : 52})

del ages["Mariam"]

for key in ages:
    print(key, ages[key])








