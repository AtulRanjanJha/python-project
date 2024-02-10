import time


print("                        WELCOME TO THE BANK                        ")
pin = int(input(f"Enter your 4-digit PIN: "))
if pin == 1234:
    print(f"\nYou have successfully logged in.")
    balance = 1000
    print("Available_balance: ",balance,"$")
    deposit = (input("\nWould you Like to deposit   y/n? \n")).lower()
    if deposit == "y":
            balance1 = (int(input("Enter the amount of money you would like to deposit:\n")))
            try:
                balance1 != int(balance1)
            except TypeError:
                 print("Error: Invalid input\n")
            balance = balance + balance1
            conformation = int(input("For conformation please enter pin: \n"))
            if conformation == pin:
                print("\nDeposited Successfully! Your new available balance is $",balance,"\n")
    elif deposit =="n":
         print(f"\nYour Available Balance is {balance}$.\n")
    else:
        print("\nINVALID  OPTION. Please try again\n.")


    loan =(input("Would you like loan: y/n?\n")).lower()
    if loan=="y":
        loantype=int(input("Do you want a personal or business loan?: \n1.Personal Loan\n2.Business Loan\nChoose option :\n"))
        if loantype == 1:
            print("You have selected Personal Loan.")
            info = input("Enter y if you want to have the info about our personal loan:\n").lower()
            if info ==  'y':
                print("Personal Loan Information:\n Interest Rate: 8%\n Tenure: 5 years\n EMI: 70$\n")
                amount = float(input("How much do you want to borrow?: "))
                roi =  amount*0.08 
                emi=amount/(6*100)
                print(f"EMI at ROI {roi} per year for 5 Years on the amount {amount}$ is",emi)
                print("proceeding with the application...")
                ok = input(f"Do You Agree to take this loan?(yes/no): \n").lower()
                if ok=='y':
                    ok_1 = int(input("Enter the pin to Proceed your Application:"))
                    if ok_1==pin:
                        print("Application Submitted Successfully.\nThankyou for choosing us.")
                        print(""".............
                              ....................
                         ............................. Processing""")
                        time.sleep(2)
                        print("Your Loan Have been approved! Congratulations!\n kindly check your mail for further details.")
                        print(f"Your available balance is {float(balance) + amount}$. THANK YOU")
                    else:
                        print("Time Out, Please try Again")
            elif info =='n':
                amount = float(input("How much do you want to borrow?: "))
                roi =  amount*0.06 
                emi=amount/(6*100)
                print(f"EMI at ROI {roi} per year for 5 Years on the amount {amount}$ is",emi)
                print("proceeding with the application...")
                print("Proceeding with the application...\n")
                ok = input(f"Do You Agree to take this loan?(yes/no): \n").lower()
                if ok=='y':
                    ok_1 = int(input("Enter the pin to Proceed your Application:"))
                    if ok_1==pin:
                        print("Application Submitted Successfully.\nThankyou for choosing us.")
                        print(""".............
                              ....................
                         ............................. Processing""")
                        time.sleep(2)
                        print("Your Loan Have been approved! Congratulations!\n kindly check your mail for further details.")
                        print(f"Your available balance is {float(balance) + amount}$. THANK YOU")

                    else:
                        print("Time Out, Please try Again")

        elif loantype ==2:
            print("You would like Bussiness Loan")
            info = input("Enter y if you want to have the info about our Business loan:\n").lower()
            if info ==  'y':
                print("Business Loan Information:\n Interest Rate: 6%\n Tenure: 5 years\n EMI: 70$\n")
                amount1 = float(input("How much do you want to borrow?: "))
                roi =  amount1*0.06 
                emi=amount1/(6*100)
                print(f"EMI at ROI {roi} per year for 5 Years on the amount {amount1}$ is",emi)
                print("proceeding with the application...")
                ok = input(f"Do You Agree to take this loan?(yes/no): \n").lower()
                if ok=='y':
                    ok_1 = int(input("Enter the pin to Proceed your Application:"))
                    if ok_1==pin:
                        print("Application Submitted Successfully.\nThankyou for choosing us.")
                        print(""".............
                              ....................
                         ............................. Processing""")
                        time.sleep(2)
                        print("Your Loan Have been approved! Congratulations!\n kindly check your mail for further ")
                        print(f"Your available balance is {float(balance) + amount1}$. THANK YOU")

                    else:
                        print("Time Out, Please try Again")
            elif info =='n':
                amount1 = float(input("How much do you want to borrow?: "))
                roi =  amount1*0.06 
                emi=amount1/(6*100)
                print(f"EMI at ROI {roi} per year for 5 Years on the amount {amount1}$ is",emi)
                print("Proceeding with the application...\n")
                ok = input(f"Do You Agree to take this loan?(yes/no): \n").lower()
                if ok=='y':
                    ok_1 = int(input("Enter the pin to Proceed your Application:"))
                    if ok_1==pin:
                        print("Application Submitted Successfully.\nThankyou for choosing us.")
                        print(""".............
                              ....................
                         ............................. Processing""")
                        time.sleep(2)
                        print("Your Loan Have been approved! Congratulations!\n kindly check your mail for further details.")
                        print(f"Your available balance is {float(balance) + amount1}$. THANK YOU")
                    else:
                        print("Time Out, Please try Again")
        else:
             pass
    elif loan =="n":
                print(f"Your available balance is {balance}$. THANK YOU")

               







else:
    print(f"\nSorry, the PIN you entered is incorrect. Please try again.\n")


