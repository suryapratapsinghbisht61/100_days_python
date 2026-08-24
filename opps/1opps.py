"""Create a Product class containing product ID, name, price, and quantity. Accept product details from the user and calculate the total bill. Apply discounts based on the purchase amount using if-else."""

class Product:
    def __init__(self):
        self.pid=int(input("enter pid "))
        self.name=input("enter name ")
        self.price=int(input("enter price "))
        self.quantity=int(input("quantity"))
        
        if self.price>1000:
           self.totalbill=self.price-(self.price/self.price*10)
        else:
           self.totalbill=self.price
    def show(self):
        print("__________Total_Bill_____________")
        print(self.pid)
        print(self.name)
        print(self.price)
        print(self.quantity)
        print(f"totalbill = {self.totalbill}")
        

c1=Product()
c1.show()

        
