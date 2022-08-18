# To generate password
import string
import random

# To pause for a few seconds
import time


# To clear the screen
from os import system


def call_from_user():
    '''This function gets called from the user inteface to implement 
        the code for the teacher interface after the menu screen'''
    def clear(i):
        '''This function clears the screen using the function system
            with argument cls present in the os library'''
        if (i == 'cleanup'):
            _ = system('cls')
    screen = "cleanup"

    # File to write questions and their corresponding correct options
    file_ques = open('questions.txt', 'w')

    # File that contains the details of students
    file_stud = open('studentfile.txt', 'w')

    # File that contains how long each student can take the test for
    file_time = open("timeperiod.txt", 'w')

    # Function to generate random password

    def rand_pass_gene(stud_details):
        '''This function generates a rondom password containing 10 letters of both cases.
            To prevent students from entering inputs for others each student is assigned a password.
            The teacher is asked to share the password generated with the student'''
        letters = string.ascii_letters
        password = (''.join(random.choice(letters) for i in range(10)))
        file_stud.write(password+"\n")
        print("\nPlease share the following password with "+stud_details)
        print("Password: ", password)
        input("\nPress enter to continue..\n\n")

    # Function to collect correct answer

    def correct_answer_input(li_options):
        '''This checks if the correct option given is one of the options
            by checking if it is present in the list of options'''
        correct_ans = input("Enter the correct option: ")
        x = correct_ans.upper()
        if x not in li_options:
            print(
                "Please enter a valid input!! \nThe correct answer must be one of the options\n")
            correct_answer_input(li_options)
        else:
            file_ques.write(x + "\n")

    # Function to take in the questions

    def question_input(no_ques, no_opt):
        '''Takes in the details of the questions'''
        print("\t\t\t----QUESTION INPUT:----")
        li_options = []
        for i in range(0, no_ques):
            ques = ""
            print("\n\nEnter question number " + str(i+1)+":  ", end="")
            while ques == "":
                ques = input()
                ques = ques.strip()
            file_ques.write(ques + "\n")
            for j in range(0, no_opt):
                option = ""
                print("Enter option " + chr(j+65)+":  ", end="")
                # To prevent taking empty input by clicking enter by mistake
                while option == "":
                    option = input()
                    option = option.strip()
                li_options.append(chr(65+j))
                file_ques.write("   "+chr(65+j)+')   ' + option + "\n")
            correct_answer_input(li_options)
        x = 0
        while (x == 0):
            try:
                time_period = int(
                    input("\nEnter the timer allocated for each student in minutes:"))
                x = 1
            except:
                print("Please enter a valid input!\n")
        file_time.write(str(60*time_period))
        print("The question details have been entered!!")
        time.sleep(2)
        clear(screen)

    # Function to collect the student details

    def student_details_input(no_stud):
        '''Takes the details of the students'''
        print("\t\t\t----STUDENT'S DETAILS:----")
        for i in range(0, no_stud):
            stud_details = ""
            print("Enter the name of student " + str(i+1) + ":  ", end="")
            # To prevent taking empty input by clicking enter by mistake
            while stud_details == "":
                stud_details = input()
                stud_details = stud_details.strip()
            file_stud.write(stud_details.upper()+"\n")
            rand_pass_gene(stud_details)
        clear(screen)

    # Main Body

    clear(screen)
    print("Hello Teacher!!!")

    print("\nEnter the following details about the quiz...")
    time.sleep(1)

    # Input for number of students
    x = 0
    while (x == 0):
        try:
            no_stud = int(input("Number of students taking the quiz:  "))
            x = 1
        except:
            print("Please enter a valid input!\n")

    # No. of questions to be entered will by no.of students multiplied by number of question per student
    x = 0
    while (x == 0):
        try:
            no_ques = no_stud * \
                int(input("Number of questions per student:  "))
            x = 1
        except:
            print("Please enter a valid input!\n")

    # Input for number of options
    x = 0
    while (x == 0):
        try:
            no_opt = int(
                input("Number of options to be given per question:  "))
            x = 1
        except:
            print("Please enter a valid input!\n")

    print("Okay now let us begin the entry of student details!!")
    input("Press enter to continue..")

    clear(screen)

    # Writes number of students into the student file
    file_stud.write(str(no_stud)+"\n")

    student_details_input(no_stud)

    print("The student details have been entered!!\n")
    print("Okay now let us begin the entry of question details!!\n\n")
    input("Press enter to continue..")
    clear(screen)

    # Writes number of questions and no of options into Q&A file
    file_ques.write(str(no_ques)+"\n"+str(no_opt)+"\n")

    question_input(no_ques, no_opt)

    print("\n\nThank you!")
    input("Please click enter to go to the user interface...")
    clear(screen)

    file_ques.close()
    file_stud.close()
    file_time.close()

    time.sleep(1)


# About the file: questions.txt
'''The question file is written in a specific format for the student interface to read it accordingly
    The format is: 
        _Total number of questions entered by teacher_
        _Number of options per question_
        _Question_ 
        _Options line by line
        _Question_
    so on..'''

# About the file: studentfile.txt
'''The student file is written in a specific format for the student interface to read it accordingly
    The format is:
        _Total number of students_
        _Name of student 1_
        _Password of student 1_
    and so on...'''

# About the file: timerperiod.txt
'''The time period file just stores how many seconds each student gets for 
    answering all the questions assigned to them'''
