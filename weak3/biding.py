data = {}
gg = True

while gg:
    ask = input("enter name ")
    askbid = int(input("what is your bid "))
    data[ask] = askbid

    are = input("are other players and they want to bid yes or no ").lower()
    if are == "yes":
        print("\n" * 333)
    else:
        gg = False

winner = ""
d = 0

for i in data:
    c = data[i]
    if d < c:
        d = c
        winner = i

print(f"highest bidder is {winner} and amount is {d}")
        
   