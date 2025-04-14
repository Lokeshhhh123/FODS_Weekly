# week 7_8:
# **********

"""Here The Questions are given in the multi-line comments using quotations and answers are given in single line comments using #
"""

"""1) Create a null vector of size 10 but the fifth value which is 1."""

# import numpy as np

# def create_special_vector():
    
#     vector = np.zeros(10)
#     vector[4] = 1
#     return vector

# result = create_special_vector()
# print(result)

"""2) Ask user to input two numbers a, b. Write a program to generate a random array of shape (a, b)
and print the array and avg of the array."""

# import numpy as np

# def generate_random_array():

#     # Get user input for array dimensions
#     a = int(input("Enter number of rows: "))
#     b = int(input("Enter number of columns: "))
    
#     # Generate random array of shape (a, b)
#     random_array = np.random.rand(a, b)
    
#     # Calculate average of the array
#     array_avg = np.mean(random_array)
    
#     return random_array, array_avg

# array, avg = generate_random_array()
# print("Generated array:")
# print(array)
# print("\nAverage of the array:", avg)

"""3) Create a vector of size 10 with values ranging from 0 to 1, both excluded."""

# import numpy as np

# def create_range_vector():

#     vector = np.linspace(0, 1, 12)[1:-1]
#     return vector

# # Test the function
# result = create_range_vector()
# print(result)

"""4) Can you create a identity matrix of shape (3,4). If yes write code for it."""

# import numpy as np

# def create_identity_matrix():
    
#     matrix = np.zeros((3, 4))
#     for i in range(min(3, 4)):
#         matrix[i, i] = 1
#     return matrix

# result = create_identity_matrix()
# print(result)


"""5) Create a 5x5 matrix with row values ranging from 0 to 4."""

# import numpy as np

# def create_range_vector():

#     vector = np.linspace(0, 1, 12)[1:-1]
#     return vector

# # Test the function
# result = create_range_vector()
# print(result)


"""5) Write a program to input an array of numbers from the user (at least 10 elements in list),
sort them and perform slicing operations to get elements between indexes such as 2-5, 5-8, 2-9. """

# import numpy as np

# def array_operations():
   
#     input_str = input("Enter at least 10 numbers separated by spaces: ")
#     input_list = [float(x) for x in input_str.split()]

#     if len(input_list) < 10:
#         print("Error: Please enter at least 10 numbers")
#         return None
 
#     array = np.array(input_list)
#     sorted_array = np.sort(array)
  
#     slice_2_5 = sorted_array[2:6]  # Elements from index 2 to 5 (inclusive)
#     slice_5_8 = sorted_array[5:9]  # Elements from index 5 to 8 (inclusive)
#     slice_2_9 = sorted_array[2:10]  # Elements from index 2 to 9 (inclusive)
    
#     return array, sorted_array, slice_2_5, slice_5_8, slice_2_9

# result = array_operations()
# if result:
#     original, sorted_arr, slice1, slice2, slice3 = result
#     print("Original array:", original)
#     print("Sorted array:", sorted_arr)
#     print("Elements between indexes 2-5:", slice1)
#     print("Elements between indexes 5-8:", slice2)
#     print("Elements between indexes 2-9:", slice3)


"""6) Create an array of random integer numbers as a numpy array,
sort them and perform operations such as reshaping of the array into matrix of feasible dimensions."""

# import numpy as np

# def reshape_array():
#     random_array = np.random.randint(1, 100, 10)
#     sorted_array = np.sort(random_array)
#     reshaped_2x5 = sorted_array.reshape(2, 5)
    
#     reshaped_5x2 = sorted_array.reshape(5, 2)
    
#     return random_array, sorted_array, reshaped_2x5, reshaped_5x2

# original, sorted_arr, reshape1, reshape2 = reshape_array()
# print("Original array:", original)
# print("Sorted array:", sorted_arr)
# print("\nReshaped into 2x5 matrix:")
# print(reshape1)
# print("\nReshaped into 5x2 matrix:")
# print(reshape2)

"""7) Write a Pandas program to add, subtract, multiple and divide two Pandas Series."""

# import pandas as pd
# def pandas_program():
   
#     series1 = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
#     series2 = pd.Series([5, 10, 15, 20, 25], index=['a', 'b', 'c', 'd', 'e'])

#     addition = series1 + series2
#     subtraction = series1 - series2
#     multiplication = series1 * series2
#     division = series1 / series2
    
#     return series1, series2, addition, subtraction, multiplication, division

# s1, s2, add, sub, mul, div = pandas_program()
# print("Series 1:")
# print(s1)
# print("\nSeries 2:")
# print(s2)
# print("\nAddition:")
# print(add)
# print("\nSubtraction:")
# print(sub)
# print("\nMultiplication:")
# print(mul)
# print("\nDivision:")
# print(div)

"""8) From the given table: 
a.	Write a query to select only the Name and Salary columns.
b.	How would you filter out all employees in the "IT" department?
c.	Write code to select employees who are older than 30.
d.	Find the average salary of employees in each department.
e.	Write code to count the number of employees in each department.
f.	Add a new column Bonus which is 10% of each employee's salary.
g.	Replace all occurrences of "HR" in the Department column with "Human Resources."
h.	 Find the employee(s) with the longest tenure (based on JoinDate).
i.	Create a new column SalaryCategory where salaries above 75,000 are categorized as "High" and the rest as "Low."
j.	Write a program to check if there are any duplicate EmployeeIDs and remove them if found.
k.	Use Pandas to calculate the median Age of all employees.
"""

# import pandas as pd
# import numpy as np
# from datetime import datetime

# def employee_operations():

#     data = {
#         'EmployeeID': [101, 102, 103, 104, 105],
#         'Name': ['John Smith', 'Alice Brown', 'Bob White', 'Emma Green', 'Charlie Red'],
#         'Department': ['IT', 'HR', 'IT', 'Finance', 'HR'],
#         'Age': [30, 28, 35, 40, 25],
#         'Salary': [70000, 60000, 80000, 90000, 55000],
#         'JoinDate': ['2018-07-15', '2020-03-10', '2016-11-01', '2012-05-25', '2021-06-01'],
#         'ExperienceYears': [5, 3, 7, 11, 2]
#     }
    
#     df = pd.DataFrame(data)
    
#     df['JoinDate'] = pd.to_datetime(df['JoinDate'])
    
#     print("Original DataFrame:")
#     print(df)
#     print("\n")
    
#     # a. 
#     name_salary = df[['Name', 'Salary']]
#     print("a. Name and Salary columns:")
#     print(name_salary)
#     print("\n")
    
#     # b.
#     non_it_employees = df[df['Department'] != 'IT']
#     print("b. Employees not in IT department:")
#     print(non_it_employees)
#     print("\n")
    
#     # c. 
#     older_employees = df[df['Age'] > 30]
#     print("c. Employees older than 30:")
#     print(older_employees)
#     print("\n")
    
#     # d.
#     avg_salary_by_dept = df.groupby('Department')['Salary'].mean()
#     print("d. Average salary by department:")
#     print(avg_salary_by_dept)
#     print("\n")
    
#     # e. 
#     employees_by_dept = df.groupby('Department').size()
#     print("e. Number of employees in each department:")
#     print(employees_by_dept)
#     print("\n")
    
#     # f. 
#     df['Bonus'] = df['Salary'] * 0.1
#     print("f. DataFrame with Bonus column:")
#     print(df)
#     print("\n")
    
#     # g. 
#     df['Department'] = df['Department'].replace('HR', 'Human Resources')
#     print("g. DataFrame with 'HR' replaced:")
#     print(df)
#     print("\n")
    
#     # h. 
#     longest_tenure = df[df['JoinDate'] == df['JoinDate'].min()]
#     print("h. Employee(s) with longest tenure:")
#     print(longest_tenure)
#     print("\n")
    
#     # i.
#     df['SalaryCategory'] = np.where(df['Salary'] > 75000, 'High', 'Low')
#     print("i. DataFrame with SalaryCategory column:")
#     print(df)
#     print("\n")
    
#     # j. 
#     print("j. Checking for duplicate EmployeeIDs:")
#     duplicates = df[df.duplicated('EmployeeID')]
#     if len(duplicates) > 0:
#         print(f"Found {len(duplicates)} duplicates")
#         df = df.drop_duplicates('EmployeeID')
#         print("After removing duplicates:")
#         print(df)
#     else:
#         print("No duplicate EmployeeIDs found")
#     print("\n")
    
#     # k. 
#     median_age = df['Age'].median()
#     print(f"k. Median Age of all employees: {median_age}")
    
#     return df

# # Test 
# result_df = employee_operations()