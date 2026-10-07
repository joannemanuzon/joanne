# Homework 5

# Homework 1 + 2 Review

# 2.1: Vocabulary Review

# 1. Git is a tool installed into a computer to track code changes and GitHub is a website that holds Git repositories 

# 2. The terminal is the program while the command line is the text area where you write commands.

# 3. A local repository is a Git-tracked project folder stored in your machine. A remote repo is the version of your project hosted on a platform
#    like GitHub and do not typically contain a working directory.

# 4. Version control means using a system that tracks every change made to a project's files. 

# 5. The staging area is where changes sit before they are committed.

# 6. Git add moves changes into the staging area

# 7. Git commit saves the changes in the staging area to the repo

# 8. Git push uploads local commits to a remote repository

# 9. Git status shows the current state of the repository

# 10. Git pull downloads new commits from a remote repo and merges them into the current branch

# 11. pwd stands for print working directory and outputs the full path of the directory you are currently in

# 12. ls lists the files and directories in your current location

# 13. cd changes the directory you are currently in

# 14. nano is a text editor that is run inside the terminal

# 15. touch either creates a new file or updates the timestamp of an existing file 

# 16. mv either moves a file or renames a file

# 17. rm removes a file 

# 18. cat prints the contents of a file


# 2.2: Directory Tree

# 1. pwd
# 2. ls
# 3. cd .. and cd brianna_repo
# 4. mv homework.py ../judy_decal/homework
# 5. cd ../brianna_repo
# 6. use cat
# 7. git add, git commit -m "desc", git push
# 8. Judy needs to pull the remote changes first, merge them, then push again

# Homework 3 Review

# 3.1 Data Types 

def checkdata(input):
    if type(input) == float:
        return("float")
    elif type(input) == str:
        return("string")
    elif type(input) == int:
        return("integer")
    elif type(input) == bool:
        return("boolean")
    else:
        return("Unknown. Try again")

print(checkdata(3.14))
print(checkdata(True))

def evenorodd(num):
    if num % 2 == 0:
        return("even")
    else:
        return("odd")

print(evenorodd(7))
print(evenorodd(10))

# 4: Loops

numbers = [1, 2, 3, 4, 5]

def sumwithloops(numbers):
    sum = 0
    for num in numbers:
        sum += num

    return(sum)

print(sumwithloops(numbers))

# Homework 5 Review

# 5.1 Lists

list = ["a" , "b" , "c"]

def duplicatelist(list):
    duplicate = []
    
    for item in list:
        duplicate.append(item)
        duplicate.append(item)

    return(duplicate)

print(duplicatelist(list))

# 5.2 Debugging

def square(num): # Missing a colon after the square(num)
    return num * num

print(square(3))

# 6 Favorite Function

# 5.1 Lists

list = ["a" , "b" , "c"]

def duplicatelist(list):
    duplicate = []
    
    for item in list:
        duplicate.append(item)
        duplicate.append(item)

    return(duplicate)

print(duplicatelist(list))

