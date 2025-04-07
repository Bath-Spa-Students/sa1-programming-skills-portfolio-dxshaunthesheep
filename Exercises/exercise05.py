# Dictionary mapping month numbers to days in that month
month_days = {
    1: 31,   
    2: 28,   
    3: 31,   
    4: 30,   
    5: 31,   
    6: 30,   
    7: 31,  
    8: 31,   
    9: 30,   
    10: 31,  
    11: 30,  
    12: 31   
}
#We made a dictionary called month_days in where the keys are the month numbers and values are the number of days in their corresponding month. 


#Using try-except block to handle non numeric values inputted by the user 
try:
    no_of_month = int(input("Enter a month number (1-12): "))
    
    #Using input to get the user's input and using int to change the input into an integer
    #Checks if input is valid
    if 1 <= no_of_month <= 12:
        days = month_days[no_of_month]

        #Displays the result
        print(f"It has {days} days.")
    else:
        print("Error! Please enter a number between 1 and 12.")
        
except ValueError:
    print("Error! Please enter a number between 1 and 12.")

#The program wil handle invalid inputs or non numeric values by displaying the suitable error prompts. 