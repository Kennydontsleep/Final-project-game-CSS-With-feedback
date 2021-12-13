def start():
    print("you have arrived to where your wife is being held captive")
    ans = input("what will you want to do (keep exploring the game/fight villagers)?")
    if ans.lower() == "keep exploring":
        print("ok, that's fine go back and keep exploring")
    answer = "fight villagers"
    while answer == "what will you want to do keep exploring the game":
                answer = input("what will you want to do (keep exploring the game/fight villagers)?")

    if ans.lower() == "fight villagers":
        print("ok, go and approach the front gate")
    ans = input("press r1 to take out your weapon")
    if ans.lower() == "r1":
        print("well, I believe that's the last of them, good job ")
    while ans.lower() != 'y':
        ans = input("would you now like to go and get your wife (y/n)?")

    if ans.lower() == "y":

        ans = input("press x to scream for your wife")
        print("hellen!!!, hellen do you hear me!!!")
        print("I am over here")
        print("player approaches her, and kisses her")
