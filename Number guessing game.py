import random
print("Welcome to the Game")

answer = random.randint(1,50)



def easy_mode():
    try:
        num= int(input("Choose a number under 50 "))

        if num == answer:
            print("You've won!")
        elif num< answer:
            print(" You have to go higher.")
            easy_mode()
        elif num> answer:
            print("You have to go lower")
            easy_mode()

    except ValueError:
        print("Please choose a number!")




def hard_mode():
    try:
        print(("Choose a number under 50"))
        print("You have 5 tries")
        tries= 0
        while tries < 5:
            num= int(input("> "))
            if num == answer:
                print ("You have won!")
                break

            elif num < answer:
                print ("You have to go higher")
                tries+=1
                if tries == 5:
                    print("You have failed this game.")
                else:
                   print ("Try again.")

            elif num> answer:
                print ("You have to go lower")
                tries+=1
                if tries == 5:
                    print("You have failed this game.")
                else:
                    print("Try again.")

    except ValueError:
        print("Please enter a number!")



def pre_game():
    print("What mode would you like to choose? ")
    print("""Press 1 for easy mode, 2 for hard mode, 3 for help""")
    choice= int(input("> "))

    if choice == 1:
        easy_mode()
    elif choice== 2:
        hard_mode()
    if choice == 3:
        print (" Easy mode gives you unlimited tries and hardmode has a 5 try limit,")
        pre_game()
pre_game()











