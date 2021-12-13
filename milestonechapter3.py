import time
import milestonechapter4


def milestonech3():
    print("Entering the chapter 3 module ")
    print("*" * 67)
    print("**                                                               **")
    print("**               CHAPTER 3  IS STARTING                          **")
    print("**                                                               **")
    print("*" * 67)

    time.sleep(2)

    print("\nWelcome to chapter 3")
    print("\nI hope you are ready to continue.")
    time.sleep(2)
    exit()


def chap3_intro():

    print("*" * 67)
    print("**                                                               **")
    print("**                                                               **")
    print("**               CHAPTER 3 INTRO                                 **")
    print("**                                                               **")
    print("**                                                               **")
    print("*" * 67)

    print("its starting to get late with a lot of wind.\n ")
    time.sleep(2)
    print("\nExiting from chapter 3 introduction  \n ")
    time.sleep(2)


def first_cluech3():
    print("option 1:first clue ...")
    print("*" * 67)
    print("**                                                               **")
    print("**               First clue in chapter 3 module IS STARTING      **")
    print("**                                                               **")
    print("*" * 67)

    print("Look,there appears to be a something on the ground.\n-----\n")
    time.sleep(2)
    travel = input("Lets take a closer look, maybe she dropped it for you to find.(Y): ")
    if travel.upper() == 'Y':
        print("You found a necklace. Clue found. Exiting from first clue in chapter 3 function\n\n ")
        done = True
    return done


def travel_east():
    print("option 2: East function is started...\n")
    print("*" * 67)
    print("**                                                               **")
    print("**               east MODULE IS STARTING                         **")
    print("**                                                               **")
    print("*" * 67)

    time.sleep(2)
    print('I think we should keep moving east to see if we can find anymore clue or just take a brake.\n ')

    print("Exiting from East function")
    done = True
    return done


def taking_break():
    print("option 3: taking break function is started...")
    print("*" * 67)
    print("**                                                               **")
    print("**               Break MODULE IS STARTING                                         **")
    print("*" * 67)

    print("Look, there appears to be a place to set camp. Maybe you should take a rest.\n-----\n")
    time.sleep(2)
    travel = input("you should make a camp.(Y): ")
    if travel.upper() == 'Y':
        print(" Go to sleep, maybe tomorrow we find something else.\n\n ")
        time.sleep(2)
        print("Chapter 4 will be started .....")
        done = False
    else:
        done = True
    return done


def choose_action3():
    print('*'*100)
    print("You can choose one of the following actions\n")
    print("1. Keep traveling.")
    print("2 travel east")
    print("\n3. Take a break")
    print('*' * 100)
    time.sleep(2)


def action3():
   choose_action3()
   print("" * 80)
   option = input("Please enter any number to start or exit with q ---->  ")
   while option != 'q':
        if option == '1':
           result = first_cluech3()
        if option == '2':
            result = travel_east()
        if option == '3':
            result = taking_break()
        else:
            print("\ninvalid option. please try again. ")
        if result == True:
           time.sleep(2)
           choose_action3()
           option = input("\nPlease enter any number to start of exit for q ---->  ")
        else:
            break
   return result


def ch3():
    print("Hey!! You are in chapter 3")
    chap3_intro()
    if action3() == False:
       milestonechapter4.ch4()






















































