import time
import chept2


def Hunting ():
    print("option 1: Hunting function is started...")
    print("*" * 67)
    print("**                                                               **")
    print("**               TALK MODULE IS STARTING                         **")
    print("**                                                               **")
    print("*" * 67)

    print(" Hello,Honey can you please help me and get some food, you need to go hunting\n-----\n")
    time.sleep(1)
    travel = input("Do you want to go Hunting(Y/N): ")
    if travel.upper() == 'Y':
        print("Exiting from Hunting function\n\n ")
        time.sleep(1)
        print("Chapter 2 will be started .....")
        done = False
    else:
        done = True
    return done


def task():
    print("option 3: task function is started...\n")
    print("*" * 67)
    print("**                                                               **")
    print("**               TASK MODULE IS STARTING                         **")
    print("**                                                               **")
    print("*" * 67)

    time.sleep(2)
    print('You can help some local villagers\n ')
    time.sleep(2)
    choice = input("\n Choose one of tasks in the list: task1-->1, task2-->2, None\n")
    if choice == '1':
        print("\nYou decided to help them with their laundry ")
        done = True
    elif choice == '2':
         print("\nYou helped with cooking  ")
         done = True

    time.sleep(2)
    return done

    print("Exiting from task function ")
    done = True
    return done


def fetch_water():
    print("option 2: fetch water function is started...")
    print("*" * 67)
    print("**                                                               **")
    print("**               fetching water MODULE IS STARTING                     **")
    print("**                                                               **")
    print("*" * 67)

    print("We are running short on water, can you please go fetch some.")
    time.sleep(2)
    travel = input("Do you want to go fetch water? y/n")
    go = travel.upper()
    if go == 'Y':
        print("Ok, going to fetch water ")
        time.sleep(2)
        done = True
    else:
        print("Exiting from fetching water")
        done = True
    return done



def choose_action():
    print('*'*100)
    print("You can choose one of the following actions\n")
    print("1. Go hunting.")
    print("\n2. fetch water.")
    print('*' * 100)
    time.sleep(2)


def action():
   choose_action()
   print("" * 80)
   option = input("Please enter any number to start of exit for q ---->  ")
   while option != 'q':
        if option == '1':
           result = Hunting()
        elif option == '2':
            result = fetch_water()

        else:
            print("\ninvalid option. please do again. ")
            result = False
        if result == True:
           time.sleep(1)
           choose_action()
           option = input("\nPlease enter any number to start of exit for q ---->  ")
        else:
            break
   return result


def chap1_intro():

    print("Enter chapter 1 introduction\n ")
    print("*" * 67)
    print("**                                                               **")
    print("**                                                               **")
    print("**               CHAPTER 1 INTRO                                 **")
    print("**                                                               **")
    print("**                                                               **")
    print("*" * 67)

    print("it was a sunny day, the sun was at its brightest.")
    time.sleep(1)
    print("\nExiting from chapter 1 introduction  \n ")
    time.sleep(1)

def ch1(name):
    print("Hey {} !! You are in chapter 1".format(name))
    chap1_intro()
    if action() == False:
        chept2.ch2()

