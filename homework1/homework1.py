# File: homework1.py
# ---Variables and Data Types---
a = 10
print(a)
print(type(a)) # a is an integer, a whole number with no decimals

b = 1.5
print(b)
print(type(b)) # b is a float, a number with decimals

c = 3j
print(c)
print(type(c)) # c is a complex number, a number with a real and imaginary part

d = "hello"
print(d)
print(type(d)) # d is a string, a sequence of characters

e = [1, 2, 3]
print(e)
print(type(e)) # e is a list, an ordered collection of items

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f)) # f is a dictionary, a collection of key-value pairs

g = (1, 2)
print(g)
print(type(g)) # g is a tuple, an ordered collection of items that cannot be changed

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) # h is a list, an ordered collection of items

i = True
print(i)
print(type(i)) # i is a boolean, a value that can be either True or False

j = None
print(j)
print(type(j)) # j is a NoneType, a special type that represents the absence of a value

k = [True, "blue", 12]
print(k)
print(type(k)) # k is a list, an ordered collection of items

l = str(14)
print(l)
print(type(l)) # l is a string, a sequence of characters

m = 1e4
print(m)
print(type(m)) # m is a float, a number with decimals

'''

1. I found 9 different data types in the code above.

2. Float, string, list, dictionary, tuple, boolean, NoneType, complex, integer

3. The variables that have the same data types are:
- b and m are both floats
- d and l are both strings
- e and h are both lists

4. The data type of l is a string, as it was created using the str() function which converts the integer 14 into a string.

'''

n = frozenset(["red", "green", "blue"])
print(n)
print(type(n)) # n is a frozenset, an unordered collection of unique items that cannot be changed

print(10 > 9) # This will print True, as 10 is greater than 9

print(10 == 9) # This will print False, as 10 is not equal to 9

print (10 <= 9) # This will print False, as 10 is not less than or equal to 9

bool("abc") # This will return True, as non-empty strings are considered True in boolean context

bool(123) # This will return True, as non-zero numbers are considered True in boolean context

bool(["apple", "banana", "cherry"]) # This will return True, as non-empty lists are considered True in boolean context

bool(True) # This will return True, as the boolean value True is considered True in boolean context

bool(False) # This will return False, as the boolean value False is considered False in boolean context

bool(0) # This will return False, as the number 0 is considered False in boolean context

bool("") # This will return False, as empty strings are considered False in boolean context

bool(" ") # This will return True, as non-empty strings (even if they contain only whitespace) are considered True in boolean context

bool(()) # This will return False, as empty tuples are considered False in boolean context

bool({}) # This will return False, as empty dictionaries are considered False in boolean context

bool({}) # This will return False, as empty sets are considered False in boolean context

bool(True and False) # This will return False, as the boolean expression evaluates to False

bool(True and True) # This will return True, as the boolean expression evaluates to True

bool(False and False) # This will return False, as the boolean expression evaluates to False

bool(True or False) # This will return True, as the boolean expression evaluates to True

bool(True or True) # This will return True, as the boolean expression evaluates to True

bool(False or False) # This will return False, as the boolean expression evaluates to False

bool(not False) # This will return True, as the boolean expression evaluates to True

bool(not True) # This will return False, as the boolean expression evaluates to False

'''
Questions:

1. I noticed that non-empty lists and non-empty strings are considered True in boolean context, while empty lists and empty strings are 
considered False. This is an important aspect of how Python evaluates truthiness.

2. What surprised me most is that even a string with just a space (" ") is considered True in boolean context, while an empty string ("") 
is considered False. This highlights the importance of understanding how different data types are evaluated in boolean expressions.

'''

print(bool(42)) # This will return True, as non-zero numbers are considered True in boolean context

print(bool(0)) # This will return False, as the number 0 is considered False in boolean context

print(10 + 5) # This will print 15, + performs addition

print(10 - 5) # This will print 5, - performs subtraction

print(2 * 4) # This will print 8, * performs multiplication

print(6 / 3) # This will print 2.0, / performs division and returns a float

print(5 % 2) # This will print 1, % performs modulus operation and returns the remainder of the division

print(3 ** 2) # This will print 9, ** performs exponentiation (3 raised to the power of 2)

print(15 // 2) # This will print 7, // performs floor division and returns the largest integer less than or equal to the division result

print(5 == 2) # This will print False, == checks for equality

print(10 != 10) # This will print False, != checks for inequality

print(2 < 5)# This will print True, < checks if the left operand is less than the right operand

print(12 > 5) # This will print True, > checks if the left operand is greater than the right operand

print(5 <= 6) # This will print True, <= checks if the left operand is less than or equal to the right operand

print(1 >= 10) # This will print False, >= checks if the left operand is greater than or equal to the right operand

x = 5

x += 5 
print(x) # This will print 10, x is incremented by 5

x -= 4 
print(x) # This will print 6, x is decremented by 4

x *= 3
print(x) # This will print 18, x is multiplied by 3

'''

Questions:

1. The and operator returns True only if both operands are True. 

bool(True and True) This will return True, as both operands are True

bool(True and False) This will return False, as one of the operands is False


2. The or operator returns True if at least one of the operands is True. 

bool(True or False) This will return True, as one of the operands is True

bool(False or False) This will return False, as both operands are False

3. The not operator negates the boolean value of the operand. 

bool(not True) This will return False, as the operand is True and negating it results in False

bool(not False) This will return True, as the operand is False and negating it results in True

4. Assignment operators are used to modify the value of a variable.

'''

my_string = "Hello"
print(my_string) # This will print "Hello"

print(my_string[0]) # This will print "H", the first character of the string

print(my_string[1]) # This will print "e", the second character of the string

print(my_string[2]) # This will print "l", the third character of the string

print(my_string[3]) # This will print "l", the fourth character of the string

print(my_string[4]) # This will print "o", the fifth character of the string

print(my_string[-1]) # This will print "o", the last character of the string

print(my_string[1:3]) # This will print "el", the substring from index 1 to 2 (3 is not included)

print(my_string[0:5:2]) # This will print "Hlo", the substring from index 0 to 4 with a step of 2

len(my_string) # This will return 5, the length of the string

print(my_string + " goodbye") # This will print "Hello goodbye", the concatenation of two strings

print(my_string * 7) # This will print "HelloHelloHelloHelloHelloHelloHello", the string repeated 7 times

'''

Questions:

1. Slicing is when you extract a portion of a string (or other sequence types) by specifying a start index, an end index, 
and an optional step. For example, my_string[1:3] extracts the substring from index 1 to 2.

'''

name = "Oski"
print("Hello, my name is " + name) # This will print "Hello, my name is Oski", concatenating the string with the variable

name = "Oski"
print(f"Hello, my name is {name}") # This will print "Hello, my name is Oski", as the variable name is being evaluated within the string

'''

3. The difference between the first and second print statements is that the first one concatenates the string with the variable 
name, while the second one uses an f-string to evaluate the variable name within the string. 
F-strings are more readable and efficient for including variables in strings.

'''

'''

cd
Changes directories. Use it to move from one folder to another. 
Example: cd Desktop

ls
Returns a list of files and directories in the current directory.
Example: ls Desktop

ls -a 
Returns a list of all files and directories, including hidden ones, in the current directory.
Example: ls -a Desktop

mkdir
Creates a new directory. Use it to make a new folder.
Example: mkdir new_folder

cat
Displays the contents of a file. Use it to read a file's content.
Example: cat file.txt

pwd
Returns the current working directory. Use it to see where you are in the file system.
Example: pwd

cd ..
Moves up one directory level. Use it to go back to the parent directory.
Example: cd ..

cd . 
Refers to the current directory. Use it to stay in the same folder.
Example: cd .

cd ~
Moves to the home directory. Use it to quickly return to your home folder.
Example: cd ~

cp
Copies files or directories. Use it to duplicate files or folders.
Example: cp file.txt copy_of_file.txt

mv 
Moves or renames files or directories. Use it to move a file to a different location or rename it.
Example: mv old_name.txt new_name.txt

rm
Deletes files or directories. Use it to remove files or folders.
Example: rm file.txt

clear
Clears the terminal screen. Use it to remove all previous commands and outputs from view.
Example: clear

grep
Searches for specific text within files. Use it to find lines that match a pattern.
Example: grep "search_term" file.txt

touch
Creates a new empty file. Use it to create a new file quickly.
Example: touch new_file.txt

rmdir
Deletes an empty directory. Use it to remove a folder that has no files in it.
Example: rmdir empty_folder

echo
Displays a line of text or a variable's value. Use it to print messages to the terminal.
Example: echo "Hello, World!"

2. ls lists visible files and directories, while ls -a lists all files and directories, including hidden ones (those starting with a dot).

3.
-l 
Displays detailed information about files and directories, such as permissions, owner, size, and modification date.
Example: ls -l

-h
Displays file sizes in a human-readable format.
Example: ls -lh

-R
Lists files and directories recursively, showing the contents of all subdirectories.
Example: ls -R

'''
