import return0_Teacher_Module
import return0_Student_Module
# Base FUNCTIONS___>>>>>>>

"""
This is a user interface which faculty or student gonna see after starting
our program this interface takes you to faculty function and student function
according to your wish, also we put a password before directing you to faculty
function so that students can't access it. 
"""


def Faculty():
    return0_Teacher_Module.call_from_user()
    Interface()


def Student():
    return0_Student_Module.call_from_user()


def Faculty_pass():
    p = input("Enter Password")
    if p == "12345":
        print("Welcome to our program")
    else:
        print("Wrong password!!!")
        print("Enter correct password")
        while True:
            Faculty_pass()
            break


def Interface():
    print("Select you category")
    print("1.Faculty \n2.Student \n3.Exit")
    x = input("Enter your choice 1 or 2\n")
    if x == "1":
        Faculty_pass()
        Faculty()
    elif x == "2":
        Student()
    elif x == "3":
        quit()
    if (x != "1" or x != "2"):
        print("Invalid input")
        while True:
            Interface()
            break


# MAIN BLOCK____>>>>>>>
Interface()
