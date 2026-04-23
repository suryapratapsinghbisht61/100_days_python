import random
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
user_card=[random.choices(cards,k=2)]
print(user_card)
computer_card=[random.choices(cards,k=2)]
for i in computer_card:
    print(i)
    break
sumckeck=sum(user_card)   
if sumckeck < 15:
    user_card.append(random.choice())
    print(user_card)
