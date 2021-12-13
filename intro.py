import milestone3chept1


def game_intro():
    print("*" * 67)
    print("**                                                                **")
    print("**                                                                **")
    print("**                            GAME INTRO                          **")
    print("**                                                                **")
    print("**                                                                **")
    print("*" * 67)


#if __name__ == '__main__':
print("*" * 67)
player = input('Enter your name ')
answer = 'n'
while answer == "n":
    answer  = input('Do you want to start a game? Enter y or n')
answer = answer.upper().strip()
if answer == 'Y':
    print("Calling the chapter 1 module\n")
    milestone3chept1.ch1(player)
