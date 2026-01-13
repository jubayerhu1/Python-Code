class Atm1:
    # constructor( special function ) -> super power
    def __init__(self):
        self.pin = "" # variable automaticaly inilization 
        self.balance = 0
        print("Program start........")


#==================================
    def menu(self):
        user_input = input(
            """ 
            Hi how can i help you ?
            1. Press 1 to create pin
            2.Press 2 to change pin
            3.Press 3 to Check balance
            5. Anythin to exit()
            ......................
            
            """)

atm= Atm1() 
atm.menu()