"""
Task 1: Identify the Greatest
Write a Python program that prompts the user to enter three numbers. The program should then identify and print out the largest number among the three.
"""
#Task 1

number  = int(input("Enter 1st number."))
number2 = int(input("Enter 2nd number."))
number3 = int(input("Enter 3rd number.")) 

largest = number, number2, number3
print(max(largest), (" is the largest number."))


"""
Task 2: Identify the Smallest
Extend your program from Task 1 to also determine the smallest number among the three and print it out.
"""

#Task 2:

smallest = number, number2, number3
print(min(smallest), (" is the smallest number."))

"""
Task 3: Equality Check
Enhance your program to handle cases where two or all of the numbers are equal. The program should display appropriate messages like "Two numbers are equal and the largest" or "All numbers are equal".
"""

#3 Equality Check
all_num = number, number2, number3
 
if number == number2:
    print("1st entry", number, " and second entry" , number2, " are equal.")
elif number == number3:
    print("1st entry", number, " and third entry", number3, " are equal.")
elif number2 == number3:
    print("2nd entry" , number2, "and third entry", number3, " are equal.")
else: 
    print("Numbers are not equal.")
    
if number and number2 and number3 % 2 == 0:
    print("All numbers are even.")
    
"""Expected Outcome: If we provide the numbers 3, 3, and 4, it should print out that "The smallest number is 3. The largest number is 4. There are two numbers equal to each other." Printing out which numbers are equal would be a great added bonus.
"""
