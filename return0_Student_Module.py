# Required MODULES_______>>>>>>>>>>>>>>>>

from os import system
import time
import random
import threading

# Required Functions_____>>>>>>>>>>>>>>>>


def call_from_user():

    # INSTRUCTIONS_students
    def inst_students(distrubution, n_optionsn):
        '''
            Function used to provide instruction 
            to the students before starting viva
        '''
        clear(1)
        print("Here are some instruction for you !!\nRead CAREFULLY")
        print("\n\n-->    You have ", distrubution, " questions to answer")
        print("-->    Each question has ", n_optionsn, " options")
        print("-->    For each correct answer you get +3")
        print("-->    For each wrong answer you get -1")
        print("-->    The quiz is timed so please use it wisely")
        print("-->    Make sure you have your password before you enter the quiz")
        print("-->    Wrong passwords will be accepted only three times")
        print("       (Be CAREFUL)You will be declare absent if you will enter")
        print("       wrong id in all your preferred chances")
        get_out = input("\n\nAll the best!!\nPress enter to continue...")

    def clear(i):                                                                    # clrscr
        '''
            Used to clear the screen when required
        '''
        if (i == 1):
            _ = system('cls')

    def countdown(time_period):
        '''Function to run the timer. 
            The while loop runs until the student runs out of time or
            until the student has answered all the questions '''                                                     # TIMER
        global timer
        timer = time_period
        while (timer > 0):
            time.sleep(1)
            timer = timer - 1
            # flag becomes 1 iff student perform all functions within the provided time
            if flag == 1:
                break
        else:
            print("\n\nOut of time\nPlease click enter..")
            time.sleep(2)

    def refresh_thread(time_period):
        '''Function to initialise the thread to run timer and start it'''                                               # Function to create a new thread for every timer activation
        countdown_thread = threading.Thread(
            target=countdown, args=(time_period,))
        countdown_thread.start()

    # READ .txt files
    def fun_to_read(file, file_legends, file_scores, file_time):
        '''
            Here we are going to fetch all the desired details that have been collceted through teacher
        '''
        n_students = file_legends.readline()  # Total number of STUDENTS collect here
        n_students = n_students[0:len(n_students)-1]
        n_studentsn = int(
            n_students)                           # """   """"  ""    """    stores here

        n_ques = file.readline()  # Total number of QUESTIONS collect here
        n_ques = n_ques[0:len(n_ques)-1]
        n_quesn = int(
            n_ques)                                   # """   """"  ""    """     stores here

        n_options = file.readline()  # Number of OPTIONS per Question have collect here
        n_options = n_options[0:len(n_options)-1]
        n_optionsn = int(
            n_options)                             # """   ""   """   "    """    stores here

        time_period = int(file_time.readline())
        li = [n_studentsn, n_quesn, n_optionsn, time_period]
        return li

    # CHECK validity_OPTIONS
    def valid_choice(li_options, user_choice):
        '''
            To check whether the input given by student is valid or not 
        '''
        for i in li_options:
            if(user_choice == i):
                return True
        return False

    def ask_ques(n_optionsn, li_ques, distribution, li_options, time_period):        # ASK !
        '''
            Let us start asking question from a single student now
            within a time limit that teacher used to define before
        '''
        sum = 0
        print("\nWelcome", current_student)  # Welcome(current student here)
        print("Let's Start--->>\n")
        time.sleep(2)

        u = distribution
        clear(1)
        global flag
        flag = 0  # To check if the student has answered all the questions and stop the timer
        refresh_thread(time_period)
        while(u != 0):  # We start to ask random questions NOW
            if(flag == 1 or timer == 0):
                break  # No more answer inputs if the student ran out of time
            ran_occ = random.choice(li_ques)
            ran_occ_ques = ran_occ[0:len(ran_occ) - 2]
            ran_occ_ans = ran_occ[len(ran_occ) - 2:len(ran_occ)-1]
            ran_occ_ans = ran_occ_ans.upper()
            print("\n")
            print(ran_occ_ques)
            user_choice = input("Your Choice :   ")
            user_choice = user_choice.upper()
            choice = 2
            # Other choices to input answer
            while(choice != 0):
                if (timer == 0):
                    break
                if(valid_choice(li_options, user_choice)):
                    if(user_choice == ran_occ_ans):
                        sum += 3
                        break
                    else:
                        sum += -1
                        break
                else:
                    print("Invalid choice !")
                    user_choice = input("Enter Again :  ")
                    user_choice = user_choice.upper()
                choice -= 1
            else:
                flag = 1
            li_ques.remove(ran_occ)
            u -= 1
        else:
            flag = 1
        file_scores.write(current_student + " : ")  # Total Score of Student
        # Put the score of the students in en empty file respectively
        file_scores.write(str(sum) + "\n")
        print("\nThankyou\nYou may leave now!!")
        # Here we clear screen now and call other random student in the remaining ones!
        li_students.remove(current_student)
        time.sleep(3)
        clear(1)

    # CHECK Presence of Student in the classroom
    def presenceOfName(current_student):
        '''
            Check the validity of student
            (Student should present in the classrom to sit in the exam)
        '''
        for i in li_students:
            if(current_student == i):
                return True
        return False

    # Details regarding QUESTIONS
    file = open('questions.txt', mode='r')
    # Students Details
    file_legends = open('studentfile.txt', mode='r')
    # Empty -->> store marks
    file_scores = open('containScore.txt', mode='a')
    # Time duration of test
    file_time = open('timeperiod.txt', mode='r')

    # Whole story begins now!!(Main Body)____>>>>>>>>>>>>>>>>>

    li_readData = fun_to_read(file, file_legends, file_scores, file_time)
    n_studentsn = li_readData[0]
    n_quesn = li_readData[1]
    n_optionsn = li_readData[2]
    # Questions equally distributed
    distribution = n_quesn // n_studentsn
    time_period = li_readData[3]

    # Compare the key(sudent) --->> value(ID)
    hold_id = {}

    li_students = []
    # All the NAME of students stored now
    for j in range(0, n_studentsn):
        sts = file_legends.readline()  # sts    -->> collects student NAME
        sts = sts[0:len(sts)-1]
        li_students.append(sts)  # Add NAME students to  li_students
        sts_id = file_legends.readline()
        sts_id = sts_id[0:len(sts_id)-1]  # sts_id -->> collects student ID
        hold_id[sts] = sts_id  # creating (NAME - ID) pair now

    li_ques = []
    for j in range(0, n_quesn):                                 # ALL QUESTIONS stored now
        stq = ""
        for i in range(0, n_optionsn + 2):
            stq += file.readline()  # stq -->> collects a question
        li_ques.append(stq)  # Add each Question -->> li_ques

    li_options = []
    # Possible correct option collect now
    for i in range(0, n_optionsn):
        want_int_form = i + 65
        want_char_form = chr(want_int_form)
        li_options.append(want_char_form)

    while(len(li_students) != 0):
        clear(1)
        # Chances to allow to enter thier Id
        cns_id = 3
        current_student = input("Enter your Name : ")
        current_student = current_student.upper()

        if(presenceOfName(current_student)):
            inst_students(distribution, n_optionsn)
            current_student_id = input("Enter ID : ")
            if(current_student_id == hold_id[current_student]):
                clear(1)

                # We start asking questions from the student now
                ask_ques(n_optionsn, li_ques, distribution,
                         li_options, time_period)
            else:
                # User have 3 chances to input ID___
                while(cns_id > 1):
                    if(current_student_id == hold_id[current_student]):
                        clear(1)

                        # We start asking questions from the student now
                        ask_ques(n_optionsn, li_ques, distribution, li_options)
                        break
                    print("\n\nID Mismatch !!\nTry again...\n")
                    current_student_id = input("Enter ID : ")
                    cns_id -= 1
                if(cns_id == 1):
                    file_scores.write(current_student +
                                      " have not give the exam\n")
                    li_students.remove(current_student)
                    clear(1)
        else:
            print(
                "Invalid input!\nYou are not allowed to sit in this exam\nGive space to others........")
            time.sleep(2)
    file.close()
    file_legends.close()
    file_scores.close()
    file_time.close()
