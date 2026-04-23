student={"surya":{"maths":20,"english":30}}
def add():
    try:
        name=input("enter studnet name ")
        sub1=[]
        sub=input("enter all subjects ").split()
        mar=int(input("enter all subject marks"))
        sub1.append(sub)
        sub1.append(mar)
        student[name]=sub1
    except Exception as e:
        print("error : " ,e)         
def display():
    for name, su in student.items():
        print(name)
        for sub, marks in su.items():
            print(sub, marks)
     
def serch():
    try:
        s = input("enter the name you want to search: ")
        if s in student:
            print("student found:", student[s])
        else:
            print("not found")
    except:
        print("somthing went wrong")

def toper():
    topper=max(student.values())
    print(topper)
       
while True:
    print("\n1.stu add  2.display 4.Search 5.exit")

    try:
        choice = int(input("enter choice: "))

        if choice == 1:
                add()
        elif choice == 2:
                display()
        elif choice == 3:
                serch()
        elif choice == 4:
                toper()
        elif choice == 5:
            print("ok by")
            break
        else:
            print("wrong choice")

    except:
            print("enter number only")