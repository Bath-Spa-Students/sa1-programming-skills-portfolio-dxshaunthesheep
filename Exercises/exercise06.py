
#Defined CORRECT_PASSWORD as a constant
CORRECT_PASSWORD = "12345"
#MAX_ATTEMTPTS sets the limit of password inputs to a number (5)
MAX_ATTEMPTS = 5

attempts = 0
#I used a while loop to keep asking the user for the password until the user gets it right or if he runs out of attempts.
#It runs as long as the number of attempts is greater than the number of maximum attemps.
while attempts < MAX_ATTEMPTS:
    #Asks the user to input a password
    user_input = input("Enter the password: ")
    attempts += 1
    #Each failed attemps will increment in the system.
    
    #Using the If-Else statement to ensure that the password the user had inputted is correct.
    if user_input == CORRECT_PASSWORD:
        print("Password correct. Access granted!")
        break
    else:
        remaining_attempts = MAX_ATTEMPTS - attempts
        if remaining_attempts > 0:
            print(f"Incorrect password. {remaining_attempts} attempt(s) remaining.")
        else:
            print("Maximum attempts reached. Authorities have been alerted!")