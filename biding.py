data={}
gg=True
while gg  :
    ask=input("enter name ")
    askbid=int(input("what is your bid "))
    are=input("are other players and they want to bid yes or no ").lower()
    if are =="yes":
        print("\n"*333)
        data[ask] = askbid
        d=0
        winner=""
        for i in data:
            c=data[i]
            if c>d:
                d=c
                winner=i
            else:
                print("")
    else:
        gg=False
        print(f"higest bidder is {winner} and amount is {d}")
        
   