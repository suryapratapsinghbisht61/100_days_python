import random
def number_guessing():
    number=random.randint(1,100)
    deficulty=input("enter deficulty hard ,easy,medium ").lower()
    
    if deficulty=="hard":
        guess_number=5
    elif deficulty=="easy":
        guess_number=10
    elif deficulty=="medium":
        guess_number=7
    else:
        print("not valid input")
        
    
     
    chanses=True
    while chanses:
        print(f"total chanses are{ guess_number}")
        guess=int(input("enter the number"))
        if guess==number:
            print("you win")
            break
        else:
            guess_number-=1
            if guess_number==0:
                chanses=False
                print("you lose")
        if number >guess:
            print("entered number is high ")
        else:
            print("entered number is too low")
number_guessing()