# week1, p2
# ***********


"""Here The Questions are given in the multi-line comments using quotations and answers are given in single line comments using #
"""

"""
1) WAP to take a number input from the user and display weather it is odd or even
"""

# num = int(input("Enter a number: "))
# if (num % 2 == 0):
    # print(f"{num} is an even number.")
# else:
    # print(f"{num} is an odd number.")
    
"""2) WAP that prompts the user for two integer values and displays the results of the first 
number divided by the second, with exactly two decimal places displayed. """

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))


# if (num2 == 0):
#     print("Error! Division by zero is not allowed.")
# else:
#     result = num1 / num2
#     print(f"Result: {result:.2f}")

"""3)WAP that will convert Celsius value to Fahrenheit."""

# unit=input("Is this  temperature in celsius or kelvin (C/F): ")
# temp=float(input("Enter the temperature: "))

# if unit=="C" or unit=="c":
#     temp= temp+ 274.15
#     unit="K"
#     print(f"Your temperature is {round(temp,1)}{unit} ")
# elif unit=="K" or unit=="k":
#     temp=temp-274.15
#     unit= "°C"
#     print(f"Your temperature is {round(temp,1)}{unit} ")
# else :
#     print(f"{unit} is not valid!")

"""4) WAP to find the Euclidean distance between two 
coordinates. Take both the coordinates from the user as input."""
# x1=int(input("Enter the first x coordinate: "))
# y1=int(input("Enter the first y coordinate: "))
# x2=int(input("Enter the second x coordinate: "))
# y2=int(input("Enter the second y coordinate: "))
# distance= ((x2-x1)**2+(y2-y1)**2)**0.5
# print(f"The Euclidean distance between the two points is {round(distance,2)}")

"""5) WAP to find the simple interest when the value of
principle, rate of interest and time period is provided by the user"""

# p=float(input("Enter the principal amount: "))
# r=float(input("Enter the rate of interest: "))
# t=float(input("Enter the time in years: "))
# SI= p*r*t/100
# print(f"The simple interest is {round(SI,2)}")

"""6) WAP program to find those numbers which are divisible by 7 and multiple 
of 5, between 1500 and 2000 (both included). """

# for i in range(1500,2000):
#     if i%7==0 and i%5==0:
#         print(f"The numbers that are divisible by 7 and multiple of 5 are: ",i)

# else:
#     print("************End of the program************")

"""7) WAP that accepts a string and calculates the number 
of digits and letters."""

# user_input = input("Enter a string: ")

# digit_count = 0
# letter_count = 0

# # Count digits and letters
# for char in user_input:
#     if char.isdigit():
#         digit_count += 1
#     elif char.isalpha():
#         letter_count += 1

# print(f"Number of digits: {digit_count}")
# print(f"Number of letters: {letter_count}")

"""8) WAP to create a number guessing game for the user. The program should ask the user to input a number. 
The program specifications are as mentioned below.
a)	The program should generate a random number for the answer.
b)	The program should prompt the user for a number input.
c)	The program should provide the feedback to the user after each guesses 
d)	The program should check the user input for 5 times and allow the users to guess 
for at most 5 times if their input don't match the answer number.
e)	If the user is not able to guess the answer within 5 times, the program should display “Game Over” message and exit. """

# import random
# rnum=random.randint(1,100)
# def guess():
 
#  num=int(input("Guess a number between 1-100: "))
#  if num==rnum:
#     print("You guessed it right!")
#  elif num<rnum:
#     print(f"Sorry, the number you guessed is too low. Try again.")
#  elif num>rnum:
#     print(f"Sorry, the number you guessed is too high. Try again.")
#  else:
#     print("Please enter a valid number.")
    
# for _ in range(4):
#     guess()
# num=int(input("Guess a number between 1-100: "))
# if num==rnum:
#     print("You guessed it right!")
# else:
#     print(f"GAME OVER. The number was {rnum}" )
    



    
    