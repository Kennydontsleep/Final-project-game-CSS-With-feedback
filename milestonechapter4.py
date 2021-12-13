import time

import milestonechapter5


def milestonech4():
    print("Entering the chapter 4 module ")
    print("*" * 67)
    print("**                                                               **")
    print("**               CHAPTER 4  IS STARTING                          **")
    print("**                                                               **")
    print("*" * 67)

    time.sleep(1)

    print("\nWelcome to chapter 4")
    print("\nI hope you are ready for what comes next.")
    time.sleep(1)
    exit()


def chap4_intro():

    print("*" * 67)
    print("**                                                               **")
    print("**                                                               **")
    print("**               CHAPTER 4 INTRO                                 **")
    print("**                                                               **")
    print("**                                                               **")
    print("*" * 67)

    print("Bright and early the next day”\n ")
    time.sleep(2)
    print("\nExiting from chapter 4 introduction  \n ")
    time.sleep(2)
    print('There seems to be a person approaching')


def Approach_person():
    print("option 1: Approach function is started...\n")
    print("*" * 67)
    print("**                                                               **")
    print("**               Approach person MODULE IS STARTING                **")
    print("**                                                               **")
    print("*" * 67)

    time.sleep(2)
    print('Wait look there appers to be sombody approaching you\n ')
    print("Hmm, i think we should see who it is")
    print("Exiting from Approaching person")
    done = True
    milestonechapter5.start()
    return done


def ignor_person():
    print("option 2: ignor person function is started...\n")
    print("*" * 67)
    print("**                                                               **")
    print("**               ignor person MODULE IS STARTING                  **")
    print("**                                                               **")
    print("*" * 67)

    time.sleep(2)
    print('Hmmm, looks like that guy wants to talk to you.\n ')
    print("I think we should go around")
    print("Exiting from ignor person function")
    done = True
    return done





def choose_action4():
    print('*'*100)
    print("You can choose one of the following actions\n")
    print("1. approach person.")
    print("2. ignor person")
    print('*' * 100)
    time.sleep(2)


def action4():
   choose_action4()
   print("" * 80)
   option = input("Please enter any number to start or exit with q ---->  ")
   while option != 'q':
        if option == '1':
            result = Approach_person()
            break
        elif option == '2':
            result = ignor_person()
            print("error please try agian ")
            choose_action4()
            option = input("Please enter any number to start or exit with q ---->  ")

        else:
            print("\ninvalid option. please try again. ")
        if result == True:
           time.sleep(2)
           choose_action4()
           option = input("\nPlease enter any number to start of exit for q ---->  ")
        else:
            break
   return result


def ch4():
    print("Hey!! You are in chapter 4")
    chap4_intro()
    if action4() == False:
       milestonechapter5.ch5()