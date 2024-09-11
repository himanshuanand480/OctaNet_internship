# OctaNet_internship Task1


import time
print("please insert your card")
print("========================================================")

"""Time taken by the atm machine as a sleep"""
time.sleep(5)
password=1234
pin=int(input("please enter your pin"))
print("========================================================")
balance=10000
while True: 
    
 if pin==password:
     print("""
          1==balance
          2==withdraw amount
          3==deposite balance
          4==exit""")
     print("========================================================")
     print("========================================================")
     try:
         option=int(input("please enter your choice"))
         print("========================================================")
         print("========================================================") 
     except:
         print("please enter the valid choice")
         print("========================================================")
         print("========================================================")
         print("========================================================")
     if option==1:
         print(f"your current balence is {balance}")
         print("========================================================")
         print("========================================================")
         print("========================================================")     
     elif option==2:
         withdraw_amount=int(input("please enter withdraw amount"))
         print("========================================================")
         print("========================================================")
         balance=balance-withdraw_amount
         print(f"{withdraw_amount} is debited from your account")
         print("========================================================")
         print("========================================================") 
         print(f"your updated current balance is {balance}")
         print("========================================================")
         print("========================================================")
         print("========================================================")
     elif  option==3:
         deposite_amount=int(input("please enter the deposit amount"))
         print("========================================================")
         balance=balance + deposite_amount
         print(f"{deposite_amount} is debited from your account")
         print("========================================================")
         print("========================================================")
         print(f"your updated current balance is {balance}")
         print("========================================================")
         print("========================================================")
     elif option==4:
         print("====================Thank you====================================")
         break
         print("====================Thank you====================================")
 else:
     print("please enter the valid pin try again, your pin is not correct")
     print("========================================================")
     print("========================================================")
     print("========================================================")
     break

