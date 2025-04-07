# I printed a label for the first sequence
print("Counting up from 0 to 50:")

# It loops from 0 to 50 with increments of +1
# Its range is (0,51) and can print numbers from 0 to (but not including) 51.
for i in range(0, 51):  
    #Each number is printed on the same line 
    print(i, end=' ')  
# A newline is added after each and every sequence for separation 
print("\n")  


# Prints text for the second sequence 
print("Counting down from 50 to 0:")

# Loops from 50 down to 0 with increments of -1
# It starts at 50, decrements by 1 each time until it stops just before -1 (0)
for i in range(50, -1, -1):  
    print(i, end=' ')
print("\n")  


# Prints text for the third sequence
print("Counting up from 30 to 50:")

# Loops from 30 to 50 with increments of +1
# The range is (30, 51). It then generates numbers from 30 to 50, going up in increments of +1
for i in range(30, 51):  
    print(i, end=' ')
print("\n")  


# Prints text for the fourth sequence
print("Counting down from 50 to 10 in steps of 2:")

# Loops from 50 down to 10 with increments of -2 
# It starts at 50, while decrementing by 2 until it reaches 9. 
# (Stops at 10 because next would be 8 which is < 9)
for i in range(50, 9, -2):  
    print(i, end=' ')
print("\n")  


# Prints text for the final sequence
print("Counting up from 100 to 200 in steps of 5:")

# Loops from 100 to 200 with increments of +5
#It starts generating numbers at 100 while incrementing by 5 until it reaches 201. 
for i in range(100, 201, 5):  
    print(i, end=' ')
# Single newline at the very end  
print()  

# End of program