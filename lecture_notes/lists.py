# Lists Syntax

numbers = [1, 2, 3, 4]
print(numbers)

fruits = ["apple", "cherries", "bananas"]
print(fruits)

# Can mix different data types in list

mixed = ["hello", 5, True, None]
print(mixed)

# Access items in a list

print(numbers[0])
print(numbers[1])
print(numbers[-1]) # Starts from the last item in the list, prints 4 (useful if number of elements in list is unknown)

# Changing items in list

fruits[0] = "grape"
print(fruits)

# Adding items to a list

numbers.append(6)
print(numbers)

# Inserting items into a list

print(mixed.insert(1, False))

print(mixed)

# Removing items

fruits.remove("bananas")
print(fruits)

fruits.pop(0)
print(fruits)

# Looping through a list

for num in numbers:
    print(num)

# Colors demo

fav_colors = ["purple", "pink", "blue"]

print(fav_colors[1])
print(fav_colors[-1])

fav_colors.append("green")

for color in fav_colors:
    print(color)

# Striding

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(nums[::1])

print(nums[1:8:2]) # Start at index 1, stop at index 8, at a step of 2

# Demo

numbs = [10, 20, 30, 40, 50, 60]
print(numbs[1:4]) # Starts at index 1, stops at index 4 (doesn't print index 4)
print(numbs[:3]) # Starts at index 0, stops at index 3 
print(numbs[3:]) # Starts at index 3, stops at end of list
print(numbs[:]) # Prints everything

numbs2 = [20, 40, 60, 80, 100]
print(nums[::2]) # Starts at beginning at a step of 2 until end
print(nums[1::2]) # Starts at index 1

# Practice Questions

list = []
i = 0

for num in range(10):
    list.append(i)
    i+= 1

print(list)