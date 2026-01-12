class atm:
    # constructor (special function) super power
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()


    def menu(self):
        
        user_input = input(
                """ 
                  --------------------
                 Hi welcome to PY ATM 
                 1. Create Pin Press 1 
                 2. Change Pin Press 2 
                 3. Checke Balance 3
                 4. Withdraw Balance 
                 5. Exit()          
                ___________________         
                 :   """)
        if user_input == "1":
            # Create pin
            self.create_pin()

        elif user_input == "2":
            # Change pin 
            self.change_pin()

        elif user_input == "3":
            # Check balance :
            self.check_balance()

        elif user_input == "4":
            # withdraw balance 
            self.withdraw_balance()
            
        elif user_input == "5":
            exit()
        else:
            print("Try to by Number ")

   #-------------------------------------
    def create_pin(self):
        user_pin = input("Enter your pin :")
        self.pin = user_pin

        user_balance = float(input("Enter your Balance :"))
        self.balance = user_balance

        print("Pin created successfully !")

        self.menu()

    #-----------------------------------------

    def change_pin(self):
        user_pin = input("Enter your old pin : ")

        if user_pin == self.pin:
            user_newPin =input("Enter your new pin : ")
            self.pin = user_newPin
        else:
            print("Your pin is incorrect !try again")

        self.menu()

    #-------------------------------------------------

    def check_balance(self):
        user_pin = input("Enter your pin : ")
        if user_pin == self.pin:
            print("Your balance is : ",self.balance)
        else:
            print("Your pin is incorrect , please try again !")

            # future can add again pin input 
        
        self.menu()
    #---------------------------

    def withdraw_balance(self):

        user_pin = input("Ente you pin : ")
        
        if user_pin == self.pin:
            amount = float(input( "Enter your amount : "))
            if amount <= self.balance:
                self.balance =self.balance - amount
                # self.balance -= amount
                print(F"Your withdraw balance is {amount}, Your new balance is {self.balance} ")
            else:
                print("Insufficient balance !")
        else:
            print("your pin is incorrect , please try again ")

        self.menu()

        

atmm = atm()
atmm.menu()