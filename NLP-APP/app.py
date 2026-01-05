import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()


#--------------base class 
# -------
class BaseModel:
    def get_model(self):
        print("----------------------program start ---------")
        try:
            
            genai.configure(api_key = os.getenv("GEMINI_API_KEY"))
            model = genai.GenerativeModel("gemini-2.5-flash")
            return model
        
        except Exception as e:
            print("here----",e)
    
   



#-----------class --------------------------
class AppFeature(BaseModel):
    def __init__(self):
        self.__database = {}
        self.first_menu()
        
    def first_menu(self):
        first_input = input("""
        Hi How would you like to proceed?c
        1. Not a member ? Register 
        2. Already a member? Login
        3. Bhai galti se aa gaya kia? exit               
                              """)
        #------------------------------------
        if first_input == "1":
            # Resiger 
            self.__register()
        elif first_input == "2":
            # login 
            self.__login()
        else:
            exit()
  #=====================================================      #----------------------------------------
        # second menu

    def second_menu(self):
        second_input = input("""
        Hi! How would you like to proceed?
        
        1.Sentiment Analysis
        2.Language Transilation
        3.Language Detection 
        4. exit()                    

        """)
    # code | summerization | conversation can add
        # 
        if second_input == "1" :
         # sentiment 
            self.__Sentiment_analysis()
        elif second_input == "2":
             # Language transilation
             self.__language_Transilation()
           
        elif second_input == "3":
             # Language detction
             self.__language_detction()
        else:
             exit()

    #===================================================
    def __Sentiment_analysis(self):
        user_text = input("Enter your text :")
        model = self.get_model()
        resposnse = model.generate_content(f"Give me the sentiment of this sentence  :{user_text}")
        #           model.generate_content(user_text3)
        result = resposnse.text
        print(result)
        self.second_menu()

    def __language_Transilation(self):
        user_text = input("Enter your text :")
        model = self.get_model()
        resposnse = model.generate_content(f"Give me Bangla transilation of this sentence :{user_text}")
        result = resposnse.text
        print(result)
        self.second_menu()


    def __language_detction(self):
        user_text = input("Enter your text :")
        model = self.get_model()
        resposnse = model.generate_content(f"Detect the language of this sentence   :{user_text}")
        result = resposnse.text
        print(result)
        self.second_menu()
         
    

   # =======================================================
    def __register(self):
        name = input ("Enter your name :  ")
        email = input("Enter your Email : ")
        password = input("Enter your password :  ")


        if email in self.__database:
                print("email already exists..")
        else:
            self.__database[email] = [name,password] #115
            print("Registration successful. Now you can login ...!")
            self.first_menu()

            
    #------------------------------

    def __login(self):
        email = input("Enter your Email : ")
        password = input("Enter your password :  ")


        if email in self.__database:
            if self.__database[email][1] == password :
                    print("login Successfull ! ")
                    # second menu
                    self.second_menu()
            else:
                    print("Incorrect password")
                    self.__login()
        else:
                print("Email not foun . please register first ")
                self.first_menu()
   


app = AppFeature()
#app.first_menu()