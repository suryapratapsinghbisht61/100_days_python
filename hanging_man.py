import random
word_list=["billionaire","money","sell_drugs","make more money"]
chosen_word=random.choice(word_list)
x=""

for i in range(len(chosen_word)):
    x+="_"
print(x)

game_end=False

live=6
hh=[]
while not game_end:
    dis=''  
    guess=input("guess the word :  ").lower()
    for i in chosen_word:
        if i == guess:
            dis+=i
            hh.append(i)
        
        elif i in hh:
            dis+=i
        
        else:
            dis+="_"
    print(dis)
    if "_" not in dis:
        game_end=True
        print("you win")
        
if live not in guess:
    live-=1
    if live ==0:
        game_end=True
        print("you lose")
        