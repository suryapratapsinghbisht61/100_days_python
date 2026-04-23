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

def cal():
    vvvv=True
    num1=int(input("ente first number "))
    while vvvv:
        for i in operations:
            print(i)
        operation_symble=input("pick an operation ")
        num2=int(input("enter second number "))
        answer=operations[operation_symble](num1,num2)
        print(f"{num1}{operation_symble}{num1}={answer}")

        ask=input(f"if you want to continue with this {answer} press 'y' in not press 'n' for new calculation ").lower()
        if ask =="y":
            num1=answer
        else:
            vvvv=False
            print("/n"*30)
            cal()
cal()