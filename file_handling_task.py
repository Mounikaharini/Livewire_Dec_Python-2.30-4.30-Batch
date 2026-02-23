def greet():
    print("--------Welcome to Zomato-------")
   
def menu():
    import time
    print()
    print("---------- MENU ----------")
    print()
    food = ["Briyani      - Rs.120",
            "Chicken Rice - Rs.100",
            "Pasta        - Rs.90",
            "Noodles      - Rs.70",
            "Exit from Order"]
    c=1
    for i in food:
        time.sleep(1)
        print(c,". ",i)
        c+=1
    ch = int(input("Enter the choice (1/2/3/4/5) :"))
    if ch==5:
        end()
        import sys
        sys.exit(0)
    else:
        q = int(input("Enter the quantity : "))
        bill(food,ch,q)
    
def bill(food,ch,q):
    amt=0
    if ch==1:
        amt=120
    elif ch==2:
        amt=100
    elif ch==3:
        amt=90
    elif ch==4:
        amt=70    
    else:
        print("Invalid Choice")
        end()
        import sys
        sys.exit(0)
    print()
    print()
    greet()
    bill = f"""\nName       :{name}
Phone Number :{phone}
Ordered Food :{food[ch-1]}
Quantity     :{q}
--------------------------------
Total Amount :{amt*q}
--------------------------------"""
    print(bill)
    f = open(r"bill.txt","a")
    f.write(bill)
    print("Order Placed Successfully 🙌")
    end()
   
def end():
    print("🙏 Thank you for visiting 👏")
    

greet()

name = input("Enter Your Name :")
phone = int(input("Enter your phone Number :"))

while(True):
    menu()


