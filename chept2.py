import time

import milestonechapter3


def milestonech2():
    print("Entering the chapter 2 module ")
    print("*" * 67)
    print("**                                                               **")
    print("**               CHAPTER 2  IS STARTING                          **")
    print("**                                                               **")
    print("*" * 67)

    time.sleep(2)

    print("\nWelcome to chapter 2")
    print("\n It was in the middle of the night you could hear the wolves in the distance.")
    time.sleep(2)
    exit()


def chap2_intro():

    print("*" * 67)
    print("**                                                               **")
    print("**                                                               **")
    print("**               CHAPTER 2 INTRO                                 **")
    print("**                                                               **")
    print("**                                                               **")
    print("*" * 67)

    print("Oh no the are other villagers raiding our camp, and they are taking women as prisoners, We need to help them.\n ")
    time.sleep(2)
    print("\nExiting from chapter 2 introduction  \n ")
    time.sleep(2)


def first_fight():
    print("option 1: first action function is started...")
    print("*" * 67)
    print("**                                                               **")
    print("**               First fight module IS STARTING                   **")
    print("**                                                               **")
    print("*" * 67)

    print("Quick you have to do something.\n-----\n")
    time.sleep(2)
    travel = input("Do you want to help your village?(Y/N): ")
    if travel.upper() == 'Y':
        print("Good job you have sacred the villagers away, but they still took your wife. Exiting from first fight function\n\n ")
        time.sleep(2)
        print("Chapter 3 will be started .....")
        milestonechapter3.ch3()
        done = False
    else:
        done = True
    return done


def journey():
    print("option 2: journey function is started ...\n")
    print("*" * 67)
    print("**                                                               **")
    print("**               journey MODULE IS STARTING                  **")
    print("**                                                               **")
    print("*" * 67)

    time.sleep(2)
    print('Oh no, the villagers have taken your wife you must go after them.\n ')
    print("Exiting from journey function")
    done = True
    return done


def choose_action2():
    print('*'*100)
    print("You can choose one of the following actions\n")
    print("1. leave.")
    print("\n2. Go and fight villagers.")
    print('*' * 100)
    time.sleep(2)


def action():
   choose_action2()
   print("" * 80)
   option = input("Please enter any number to start of exit for q ---->  ")
   while option != 'q':
        # if option == '1':
        #    result = first_fight()
        if option == '2':
            result = journey()
            first_fight()
            break
        else:
            print("\ninvalid option. please try again. ")
            result = True
        if result == True:
           time.sleep(1)
           choose_action2()
           option = input("\nPlease enter any number to start of exit for q ---->  ")
        else:
            break
   return result


def ch2():
    print("Well done!! You are in chapter 2")
    chap2_intro()
    if action() == False:
       milestonechapter3.ch3()


























































