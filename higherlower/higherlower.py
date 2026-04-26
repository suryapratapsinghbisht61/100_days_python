from higerlower_data import instagram_celebrities
import random
assert len(instagram_celebrities) == 100

fu=True
counter=0
while fu:
    x, x1 = random.sample(list(instagram_celebrities.values()), 2)
    print(f"A: {x['name']}, {x['what_they_do']} \n")
    print(f"B: {x1['name']}, {x1['what_they_do']}  \n")
    user_res=input("tell me who has higher instagram follower A or B  \n").lower()
    if user_res=="a":
        if x["followers_m"]>x1["followers_m"]:
             counter+=1
             print("correct")
        else:
            fu=False
            print(f"Game over total correct are {counter}")
                
    elif user_res=="b":
        if x["followers_m"]<x1["followers_m"]:
            counter+=1
            print("correct")
        else:
            fu=False
            print(f"Game over total correct are {counter}")
                
    else:
        print("enter valid values = A or B ")