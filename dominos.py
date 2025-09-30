#  dominos clone
import random
class dominos:
    menu={"veg":{"margerita":129,"cheese_and_corn":169,"peppi_paneer":260,"veg_loaded":210,"tomato_tangi":170},
            
            "non_veg":{'pepper_barbeque':199,'non_veg_loaded':169,'chicken_sausage':200},
            
            "snacks":{'garlic_bread':120,'zingy':59,'chicken_cheese_balls':170},
            
            "desserts":{'choco_lava':100,'mousse_cake':169},
            
            "drinks":{'coke':90,'pepsi':78,'sprite':50}
            
            }
    def __init__(self,name,email,phno):
        self.name=name
        self.email=email
        self.phno=phno
        self.login_status=False #TO VALIDATE LOGIN STATUS
        self.cart={} #to store orders
        
        #MAIN PROGRAM
        while True:
            if not self.login_status:
                print("------WELCOME TO DOMINOS 🍕 APP------")
                print("login")
                ch=input("Do you want to login? (y/n):")
                if ch=='y':
                    self.login()
            if self.login_status:        
                print("user👤:",self.name)
                print("enter 1:order")
                print("enter 2:show cart")
                print("enter 3:logout")     
                choice=int(input("Enter choice:"))
                if choice==1:
                   self.order()
                elif choice==2:
                    self.show_cart()
                elif choice==3:
                    self.logout()
                else:
                    print("Invalid choice: ")
    @staticmethod
    def validate_otp(value):
        while True:
            og_otp=random.randint(1000,9999)
            print(f"an otp has been sent to {value}")
            print(f"your dominos otp is:{og_otp}")
            otp=int(input("Enter otp:"))
            if otp==og_otp:
                print("Login successfully✅")
                return True
            print("incorrect otp enter correct otp...")
                
    def login(self):
        print("Enter 1:login with phno")
        print("Enter 2:login with email")
        ch =int(input("Enter choice:"))
        if ch==1:
            #phone no validation
            phno=int(input("Enter phno:"))
            if phno==self.phno:
                state=self.validate_otp(phno)#True
                self.login_status=state
            else:
                print("Incorrect phno")
                
        elif ch==2:
            #email validation
            email=input("Enter email:")
            if email==self.email:
                state=self.validate_otp(email)
                self.login_status=state
            else:
                print("invalid email")
        else:
            print("invalid choice")
    def order(self):
       print("------------------dominos.menu-------------")
       for category in dominos.menu:
           print(category)
       cat=input("Enter category: ")
       if cat in dominos.menu:
            d=dominos.menu[cat]
            for item in d: #display items of respective category
                print(item,'     Rs.',d[item])
            item=input("enter item: ")
            if item in d:
                q=int(input("Enter quantity: "))
                if item in self.cart:
                    self.cart[item]+=d[item]*q #var[key]=new val
                else:
                    self.cart[item]=d[item]*q
                print(f"{item} added to the cart🛒")
                print(self.cart)
            else:
                print(f'{item}is not available❌')
       else:
                print(f'(cat) is not available❌') 
    def show_cart(self):
        print("------dominos cart 🛒-----")
        if self.cart!={}:
            total_bill=0
            for item in self.cart:
                total_bill+=self.cart[item]
                print(item,'--------- Rs.',self.cart[item])
            print("Total Bill:          Rs. ",total_bill)
        else:
            print("Cart is empty please order..")
        ch=input("Do you want to place order? (y/n): ")
        if ch=='y':
            print("Thankyou 🤗 for placing the order...")
            print("your order is on the way❤️")
            self.cart=()
    def logout(self):
        ch= input("Do you want to logout? (y/n): ").lower()
        if ch=='y':
            self.login_status=False
            print("Logged out✅")
ob=dominos("monika","moni@gmail.com", 1234567899)