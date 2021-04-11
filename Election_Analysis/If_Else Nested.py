# If Else Statement: Usually wriiten in the way it is below (Lines 8 - 23):
# The first if statement tests the condition
# The following else statement and the preceding if statement are compounded to make the "elif" statement
# This sytax continues until the last else statement
# In an if-elif-else statement (Lines 25 - 38), the if, elif, and else statements are all aligned, and the conditionally executed blocks are indented.


# What is the score?
#score = int(input("What is your test score?"))

# Determine the grade.
#if score >= 90: 
#    print('Your grade is an A.')
#else: 
#    if score >= 80:
#        print('Your grade is a B.')
#    else: 
#        if score >= 70:
#            print('Your grade is a C.')
#        else: 
#            If score >= 60:
#                print('Your grade is a D.')
#            else: print('Your grade is an F.')

#IF ELIF ELSE STATEMENT BELOW:
# What is the score?
score = int(input("What is your test score?"))

# Determine the grade
if score >= 90:
    print('Your grade is an A.')
elif score >= 80: 
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else: 
    print('Your grade is an F.')
