def check_even_odd(number):
    """
    Checks whether the given number is even or odd.
    
    Args:
        number (int): The number that needs to be checked 
        
    Returns:
        str: It is a message which indicates whether a number is odd or even
        """
    # Check if the number is divisible by two with no remainder
    if number % 2 == 0:
        # Return a message saying the number is even if its even
        return f"{number} is an even number."
    else:
        # Return a message saying the number is odd if its odd
        return f"{number} is an odd number."

def main():
    """
    Main function that handles user input and output.
    Implements error handling for non-integer inputs.
    """
    # The try block is there to handle invalid inputs from the user
    try:
        # Prompts the user to enter a number and converts it into an integer
        num = int(input("Enter a number: "))
        
        # Call check_even_odd function with user's inputted number
        result = check_even_odd(num)
        
        # Prints result returned from function
        print(result)
        
    # Handle case where input cannot be converted to integer
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

# Standard Python idiom to ensure code only runs when executed directly
if __name__ == "__main__":
    # Call the main function to start program execution
    main()