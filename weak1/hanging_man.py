import random
word_list=["billionaire","money","sell_drugs","make more money"]
chosen_word=random.choice(word_list)
x=""

for i in range(len(chosen_word)):
    x+="_ "
print(x)

game_end=False

hh=[]
while not game_end:
    dis=''
    guess=input("guess the word :  ").lower()
    for i in chosen_word:
        if guess == i:
            dis+=i
            hh.append(guess)
        
        elif i in hh:
            dis+="_ "
        
        else:
            dis+="_ "
    print(dis)
    if "_ " not in dis:
        game_end=True
        print("you win")