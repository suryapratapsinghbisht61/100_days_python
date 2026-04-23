def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2    

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

operations={
    "+":add,
     "-":sub,
     "*":mul,
     "/":div
}

num1=int(input("ente first number "))
for i in operations:
    print(i)
operation_symble=input("pick an operation ")
num2=int(input("enter second number "))
print(num1,operation_symble,num1 ,"=" ,operations[operation_symble](num1,num2))



