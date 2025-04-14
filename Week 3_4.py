# Week 3_4 :
# *********** 


"""Here The Questions are given in the multi-line comments using quotations and answers are given in single line comments using #
"""

"""1) wAP with a function that accepts a string input from the user and calculates the number of uppercase 
and lowercase letters.
"""

# def count_upper_lower(s):
#     upper_count = 0
#     lower_count = 0
#     for char in s:
#         if char.isupper():
#             upper_count += 1
#         elif char.islower():
#             lower_count += 1
#     return upper_count, lower_count

# if __name__ == "__main__":
#     user_input = input("Enter a string: ")
#     upper, lower = count_upper_lower(user_input)
#     print("Number of uppercase letters:", upper)
#     print("Number of lowercase letters:", lower)

"""2) WAP to check whether the given number is prime or not"""

# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# if __name__ == "__main__":
#     number = int(input("Enter a number: "))
#     if is_prime(number):
#         print(number, "is a prime number.")
#     else:
#         print(number, "is not a prime number.")

"""3) WAP to check whether the given number is Armstrong or not"""

# def is_armstrong(n):
#     num_str = str(n)
#     num_digits = len(num_str)
#     total = sum(int(digit) ** num_digits for digit in num_str)
#     return total == n

# if __name__ == "__main__":
#     number = int(input("Enter a number: "))
#     if is_armstrong(number):
#         print(number, "is an Armstrong number.")
#     else:
#         print(number, "is not an Armstrong number.")

"""4) WAP to accept a list of names and return the sorted order of names back"""


# def sorted_names(names_list):
#     return sorted(names_list)

# if __name__ == "__main__":
#     names_input = input("Enter names separated by commas: ")
#     names_list = [name.strip() for name in names_input.split(',')]
#     sorted_list = sorted_names(names_list)
#     print("Sorted names:", sorted_list)

"""5) WAP to create a simple calculator with functions to perform basic arithmetic
    calculations including:
        A. Addition
        B. Subtraction
        C. Multiplication
        D. Division
        E. Truncated Division
        F. Modulus
        G. Exponentiation
    Each function takes two decimal parameters and returns the calculated result."""
    
# def add(a, b):
#     """Returns the addition of a and b."""
#     return a + b

# def subtract(a, b):
#     """Returns the subtraction of b from a."""
#     return a - b

# def multiply(a, b):
#     """Returns the multiplication of a and b."""
#     return a * b

# def divide(a, b):
#     """Returns the division of a by b; raises error if b is zero."""
#     if b == 0:
#         raise ValueError("Division by zero is not allowed.")
#     return a / b

# def truncated_division(a, b):
#     """Returns the truncated (integer) division of a by b; raises error if b is zero."""
#     if b == 0:
#         raise ValueError("Division by zero is not allowed.")
#     return a // b

# def modulus(a, b):
#     """Returns the modulus (remainder) of a divided by b; raises error if b is zero."""
#     if b == 0:
#         raise ValueError("Division by zero is not allowed.")
#     return a % b

# def exponentiation(a, b):
#     """Returns a raised to the power of b."""
#     return a ** b

# if __name__ == "__main__":
#     try:
#         a = float(input("Enter first number: "))
#         b = float(input("Enter second number: "))
#         print("Addition:", add(a, b))
#         print("Subtraction:", subtract(a, b))
#         print("Multiplication:", multiply(a, b))
#         print("Division:", divide(a, b))
#         print("Truncated Division:", truncated_division(a, b))
#         print("Modulus:", modulus(a, b))
#         print("Exponentiation:", exponentiation(a, b))
#     except ValueError as e:
#         print("Error:", e)

"""6) WAP that prompts the user for a series of integers and stores in a list only the 
values between 1-100, and displays the resulting list.  """

# def filter_int(integers):
#     return [num for num in integers if 1 <= num <= 100]

# if __name__ == "__main__":
#     user_input = input("Enter integers separated by commas: ")
#     try:
#         num = [int(item.strip()) for item in user_input.split(',')]
#     except ValueError:
#         print("Please ensure you enter valid integers separated by commas.")
#         exit(1)
#     filtered_num = filter_int(num)
#     print("Filtered integers (between 1 and 100):", filtered_num)

"""7) 6. WAP that prompts the user to enter a list of names and store them in a list. 
The program should display how many times the letter 'a appears within the list. """

# def count_a_in_names(names):
#     count = 0
#     for name in names:
#         count += name.lower().count('a')
#     return count

# if __name__ == "__main__":
#     names_input = input("Enter names separated by commas: ")
#     names_list = [name.strip() for name in names_input.split(',')]
#     a_count = count_a_in_names(names_list)
#     print("The letter 'a' appears", a_count, "times in the list.")

"""8) Write a program that prompts the user to enter integer values to populate two lists,
then prints messages to determine the following:
(a) Whether the lists are of the same length. 
(b) Whether the elements in each list sum to the same value. 
(c) Whether there are any values that occur in both lists
 """
 
#  def parse_input_to_int_list(prompt):
#     user_input = input(prompt)
#     try:
#         return [int(item.strip()) for item in user_input.split(',')]
#     except ValueError:
#         print("Please enter valid integers separated by commas.")
#         exit(1)
# if __name__ == "__main__":
#     list1 = parse_input_to_int_list("Enter integers for list 1 (separated by commas): ")
#     list2 = parse_input_to_int_list("Enter integers for list 2 (separated by commas): ")

#     if len(list1) == len(list2):
#         print("The two lists are of the same length.")
#     else:
#         print("The two lists are not of the same length.")

#     if sum(list1) == sum(list2):
#         print("The sums of both lists are equal.")
#     else:
#         print("The sums of the lists are not equal.")

#     common_elements = set(list1) & set(list2)
#     if common_elements:
#         print("Common values found in both lists:", common_elements)
#     else:
#         print("There are no common values between the lists.")

"""9) WAP with a function called add_daily_temp that is given a (possibly empty) dictionary 
meant to hold the average daily temperature for each day of the week, a temperature value,
and the day of the week for the recorded temperature. 
The function should then add the temperature to the dictionary only if it does not already contain a temperature for that day. 
The function should return the resulting dictionary, whether it is updated or not"""

# def add_daily_temp(temps_dict, temp, day):
#     if day not in temps_dict:
#         temps_dict[day] = temp
#     return temps_dict

# if __name__ == "__main__":
#     daily_temps = {}
#     daily_temps = add_daily_temp(daily_temps, 75.5, "Monday")
#     daily_temps = add_daily_temp(daily_temps, 80.0, "Tuesday")
#     daily_temps = add_daily_temp(daily_temps, 78.0, "Monday")
#     print("Daily Temperatures:", daily_temps)

"""10) WAP with a function named get_daily_temps that prompts the user for the average
temperature for each day of the week and returns a dictionary containing the information the user entered. """

# def get_daily_temps():
#     days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#     temps = {}
#     for day in days_of_week:
#         while True:
#             try:
#                 temp = float(input(f"Enter the average temperature for {day}: "))
#                 break
#             except ValueError:
#                 print("Please enter a valid number.")
#         temps[day] = temp
#     return temps

# if __name__ == "__main__":
#     daily_temps = get_daily_temps()
#     print("Weekly Temperatures:", daily_temps)

"""11) Create three dictionaries:
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}
(a) Write code to concatenate these dictionaries to create a new one. Create a variable 
called nums to store the resulting dictionary. 
(b) Write code to add a new key/value pair to the dictionary nums: (7, 70)
(c) Write code to update the value of the item with key 3 in nums to 80
(d) Write code to remove the third item from dictionary nums.
(e) Write code to sum all the items in the dictionary nums
(f) Write code to multiply all the items in the dictionary nums
(g) Write code to retrieve the maximum and minimum values in nums.
"""
# if __name__ == "__main__":
#     # (a) 
#     dic1 = {1: 10, 2: 20}                                           
#     dic2 = {3: 30, 4: 40}                                        
#     dic3 = {5: 50, 6: 60}
#     nums = {**dic1, **dic2, **dic3}
#     print("Initial concatenated dictionary (nums):", nums)       

#     # (b) 
#     nums[7] = 70
#     print("After adding (7, 70):", nums)

#     # (c) 
#     if 3 in nums:
#         nums[3] = 80
#     print("After updating key 3 to 80:", nums)                     

#     # (d) 
    
#     key_to_remove = list(nums.keys())[2]  
#     removed_value = nums.pop(key_to_remove)                        
#     print(f"After removing the third item (key {key_to_remove}: {removed_value}):", nums)

#     # (e) 
#     total_sum = sum(nums.values())                               
#     print("Sum of all values in nums:", total_sum)

#     # (f) 
#     product = 1
#     for value in nums.values():
#         product *= value
#     print("Product of all values in nums:", product)

#     # (g) 
#     max_value = max(nums.values())
#     min_value = min(nums.values())
#     print("Maximum value in nums:", max_value)
#     print("Minimum value in nums:", min_value)

""""12).	Create two sets: [5]
set1 = {20, 40, 60}
set2 = {10, 20, 30, 40, 50, 60}
(a) Write code to perform a union of these sets. Print the length of the resulting set.
(b) Write code to perform an intersection of set1 and set2.
(c) Write code to compute the symmetric difference between set1 and set2
(d) Write code to add the value 40 to set1, did the set change?
(e) Write code to remove value 20 from set2.
"""
# dic1, dic2, dic3 = {1:10, 2:20}, {3:30, 4:40}, {5:50, 6:60}
# nums = {**dic1, **dic2, **dic3}
# nums[7] = 70
# nums[3] = 80
# del nums[3]
# sum_values = sum(nums.values())
# mul_values = 1
# for v in nums.values(): mul_values *= v
# max_val, min_val = max(nums.values()), min(nums.values())
# print("Final Dictionary:", nums)
# print("Sum:", sum_values, "Product:", mul_values, "Max:", max_val, "Min:", min_val)

"""13) Create a function called word_intersection that prompts the user for two English words, and 
displays which letters the two words have in common. """

# def word_intersection(word1, word2):
#     return set(word1) & set(word2)

# word1, word2 = input("Enter first word: "), 
# input("Enter second word: ")
# print("Common letters:", word_intersection(word1, word2))