import random
user_input=int(input("enter 1 for rock, 2 for paper, 3 for scissors "))
computer=random.choice(["rock","paper","scissors"])
print(f"you chose {user_input} and computer chose {computer}")
if user_input==1 and computer=="rock":
    print("draw")
elif user_input==1 and computer=="paper":
    print("you lose")
elif user_input==1 and computer=="scissors":
    print("you win")
elif user_input==2 and computer=="rock":
    print("you win")
elif user_input==2 and computer=="paper":
    print("draw")
elif user_input==2 and computer=="scissors":
    print("you lose")
elif user_input==3 and computer=="rock":
    print("you lose")
elif user_input==3 and computer=="paper":
    print("you win")
elif user_input==3 and computer=="scissors":
    print("draw")
else:
    print("invalid input")
