# name = "Joanne"

# print("Hello,", name)

# def say_hello(name):
#     print("Hello,", name)

# say_hello(name = "Kimberly")

# def add(a, b):
#     return a + b
# # better to return the value instead of printing to be able to save the value to a variable or use it in another function

# print(add(7, 8))

# def check_num(num):
#     if num > 0:
#         return "Positive"
#     elif num < 0:
#         return "Negative"
#     else: 
#         return "Zero"

# print(check_num(42))

# def can_vote(age, is_citizen):
#     if age >= 18 and is_citizen:
#         print("You can vote!")
#     else:
#         print("You cannot vote.")

# can_vote(19, True)

# def is_weekend(day):
#     if day == "Saturday" or day == "Sunday":
#         return "It is the weekend!"
#     else:
#         return "It is a weekday."

# print(is_weekend("Monday"))

# for i in range(10):
#     print(i) # starts from 0 goes to 9, doesn't include 10

# fruit_basket = ["lychee", "mango", "nectarines"]

# for fruit in fruit_basket:
#     print(fruit)

# def countdown(start):
#     while start > 0:
#         print("T-", start)
#         start -= 1

# countdown(10)

# list = [14,5,9,11]

# def minimum_value(list):
#     return min(list)

# print(minimum_value(list))

# Create a function to determine if a positive integer is a prime number

def isprime(num):
    if num <= 0 or type(num) != int:
        return "Try again. Choose a new number."
    else:
        if num == 1:
            return "Neither."
        elif num == 2:
            return "Is a prime number."
        else:
            if num % 2 == 0:
                return "Composite number."
            else:
                for i in range(1, num):
                    if num % i == 0:
                        return "Composite number."
                    else:
                        return "Prime number."

print(isprime(9))