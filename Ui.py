# Name:         Trace Sweeney
# Email:        sweenetr@oregonstate.edu
# Description:  Microservice which returns the amount of capitol a user would
#               need to add monthly to an account to reach their financial goals
# INPUT:        R = annual rate of return, G = Savings goal, P = Starting principal, Y = years to save 
# OUTPUT:       Monthly contribution amount


import time

while True:
    #get input from user to generate image or exit
    usr_input = input("Press 1 to find out how much you need to save monthly to reach your financial goals or press 2 to exit: ")
    
    #if they want to generate image
    if usr_input == "1":
        r_as_percent = input("Enter your expected annual interest rate: ")
        r_value = str(int(r_as_percent)/100)
        g_value = input("Enter the amount you would like to have saved: $")
        p_value = input("Enter the amount you already have saved: $")
        y_value = input("Enter how many years before you want to reach your goal: ")
        #clear the user_input.txt file and the monthly_savings_amount.txt file
        user_input_file = open("user_input.txt", "r+")
        user_input_file.truncate()
        user_input_file.close()
        monthly_savings_file = open("monthly_savings_amount.txt", "r+")
        monthly_savings_file.truncate()
        monthly_savings_file.close()
        #write run to the prng-service file for the prng.py program
        user_input_file = open("user_input.txt", "w")
        user_input_file.write(f"{r_value},{g_value},{p_value},{y_value}")
        user_input_file.close
        user_input_file = open("user_input.txt", "w")
        user_input_file.close
        user_input_file = open("user_input.txt", "r")
        user_input_file.close
        time.sleep(3)
        #read the file for the random number amount
        monthly_savings_amount_file = open("monthly_savings_amount.txt")
        file_contents = monthly_savings_amount_file.read()
        print(f'The amount you need to save per month is: ${file_contents}')
        monthly_savings_amount_file.close()

    
    elif usr_input == "2":
        exit()

    else:
        print("unknown option")