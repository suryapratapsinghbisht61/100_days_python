import random

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M","N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m","n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+", "@", "^"]

user_input_letters=int(input("enter the number of letter you want in your password =  "))
user_input_numbers=int(input("enter the number of number you want in your password =  "))
user_input_symbols=int(input("enter the number of special letter you want in you password =  "))

pasword_list=[]
c=""
for _ in range(0,user_input_letters ):
    pasword_list.append(random.choice(letters))
    
for _ in range(0,user_input_numbers ):
    pasword_list.append(random.choice(numbers))
    
for _ in range(0,user_input_symbols ):
    pasword_list.append(random.choice(symbols))

random.shuffle(pasword_list)
for i in pasword_list:
    c+=i

print(c)
