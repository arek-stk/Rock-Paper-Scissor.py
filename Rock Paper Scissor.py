import random
choices = ('r','p','s')
user_input = input("Rock, Paper or Scissor? (r/p/s): ").lower()
computer = random.choice(choices)
if user_input not in choices:
    print("invalid choice!")
else:
    if (user_input == "r") and (computer =="p"):
        print(computer)
        print("YOU LOST")
    elif (user_input == "r") and (computer == "s"):
        print(computer)
        print("YOU WON")
    elif (user_input == "s") and (computer =="r"):
        print(computer)
        print("YOU LOST")
    elif (user_input == "s") and (computer =="p"):
        print(computer)
        print("YOU WON")
    elif (user_input == "p") and (computer =="s"):
        print(computer)
        print("YOU LOST")
    elif (user_input == "p") and (computer =="r"):
        print(computer)
        print("YOU WON")
    elif (user_input == "r") and (computer =="r"):
        print(computer)
        print("Equal")
    elif (user_input == "s") and (computer == "s"):
        print(computer)
        print("Equal")
    elif (user_input == "p") and (computer == "p"):
        print(computer)
        print("Equal")
