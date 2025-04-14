# Week 5_6:
#***********


"""Here The Questions are given in the multi-line comments using quotations and answers are given in single line comments using #
"""

"""1) WAP to count the number of lines, words, and characters in a text file."""

# def count_file_statistics(filename):
#     try:
#         with open(filename, 'r') as file:
#             content = file.read()
#             char_count = len(content)
      
#             file.seek(0)
        
#             lines = file.readlines()
#             line_count = len(lines)
            
#             word_count = len(content.split())
            
#             return (line_count, word_count, char_count)
    
#     except FileNotFoundError:
#         print(f"Error: The file '{filename}' was not found.")
#         return (0, 0, 0)
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return (0, 0, 0)

# def main():
   
#     filename = input("Enter the filename to analyze: ")

#     lines, words, chars = count_file_statistics(filename)
#     if lines > 0 or words > 0 or chars > 0:
#         print("\nFile Statistics:")
#         print("-" * 20)
#         print(f"Number of lines: {lines}")
#         print(f"Number of words: {words}")
#         print(f"Number of characters: {chars}")

# if __name__ == "__main__":
#     main()

"""2) WAP to copy the contents of one file to another."""

# def copy_file(source_file, destination_file):
#     try:
#         with open(source_file, 'r') as source:
#             content = source.read()
#             with open(destination_file, 'w') as destination:
#                 destination.write(content)
                
#             print(f"File copied successfully from '{source_file}' to '{destination_file}'")
#             return True
            
#     except FileNotFoundError:
#         print(f"Error: Source file '{source_file}' not found.")
#         return False
#     except PermissionError:
#         print(f"Error: Permission denied. Check if you have proper access rights.")
#         return False
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return False

# def main():
#     source = input("Enter the source filename: ")
#     destination = input("Enter the destination filename: ")
#     copy_file(source, destination)

# if __name__ == "__main__":
#     main()

"""3) WAP to find and replace a specific word in a file with another word."""

# def find_and_replace(filename, word_to_find, replacement_word):
#     try:
#         with open(filename, 'r') as file:
#             content = file.read()
    
#         occurrences = content.count(word_to_find)
        
#         if occurrences == 0:
#             print(f"The word '{word_to_find}' was not found in the file.")
#             return 0
        
#         modified_content = content.replace(word_to_find, replacement_word)
        
#         with open(filename, 'w') as file:
#             file.write(modified_content)
            
#         print(f"Successfully replaced {occurrences} occurrence(s) of '{word_to_find}' with '{replacement_word}'")
#         return occurrences
        
#     except FileNotFoundError:
#         print(f"Error: The file '{filename}' was not found.")
#         return 0
#     except PermissionError:
#         print(f"Error: Permission denied. Check if you have proper access rights.")
#         return 0
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return 0

# def main():
#     filename = input("Enter the filename: ")
#     word_to_find = input("Enter the word to find: ")
#     replacement_word = input("Enter the replacement word: ")
    
#     find_and_replace(filename, word_to_find, replacement_word)

# if __name__ == "__main__":
#     main()

"""4) Implement a program to read a CSV file and display its contents in a tabular format"""

# import csv

# def display_csv(filename):
#     try:
#         with open(filename, 'r', newline='') as file:
#             csv_reader = csv.reader(file)
#             rows = list(csv_reader)
            
#             if not rows:
#                 print("The CSV file is empty.")
#                 return False
            
         
#             col_widths = []
#             for row in rows:
#                 while len(col_widths) < len(row):
#                     col_widths.append(0)
                
#                 for i, cell in enumerate(row):
#                     col_widths[i] = max(col_widths[i], len(str(cell)))
            
#             print("\nCSV File Contents:")
#             print("-" * (sum(col_widths) + 3 * len(col_widths) + 1))
            
#             for i, row in enumerate(rows):
#                 row_str = "| "
#                 for j, cell in enumerate(row):
#                     if j < len(col_widths):
#                         row_str += str(cell).ljust(col_widths[j]) + " | "
#                 print(row_str)
                
#                 if i == 0:
#                     print("-" * (sum(col_widths) + 3 * len(col_widths) + 1))
            
#             print("-" * (sum(col_widths) + 3 * len(col_widths) + 1))
#             return True
            
#     except FileNotFoundError:
#         print(f"Error: The file '{filename}' was not found.")
#         return False
#     except csv.Error as e:
#         print(f"CSV Error: {e}")
#         return False
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return False

# def main():
#     filename = input("Enter the CSV filename to display: ")
    
#     display_csv(filename)

# if __name__ == "__main__":
#     main()


"""5) Develop a program that counts the occurrence of each word in a file"""

# import re
# import string

# def count_word_occurrences(filename):
#     try:
#         word_counts = {}
#         with open(filename, 'r') as file:
#             content = file.read().lower()
            
#             for punct in string.punctuation:
#                 content = content.replace(punct, ' ')
            
#             words = content.split()
#             for word in words:
#                 word = re.sub(r'[^a-zA-Z0-9]', '', word)
                
#                 if not word:
#                     continue
                    
#                 if word in word_counts:
#                     word_counts[word] += 1
#                 else:
#                     word_counts[word] = 1
        
#         return word_counts
        
#     except FileNotFoundError:
#         print(f"Error: The file '{filename}' was not found.")
#         return {}
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return {}

# def display_word_counts(word_counts):
#     if not word_counts:
#         print("No words to display.")
#         return
    
#     sorted_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    
#     max_word_len = max(len(word) for word in word_counts.keys())
    
#     print("\nWord Occurrences:")
#     print("-" * (max_word_len + 15))
#     print(f"{'Word'.ljust(max_word_len)} | Occurrences")
#     print("-" * (max_word_len + 15))
    
#     for word, count in sorted_counts:
#         print(f"{word.ljust(max_word_len)} | {count}")
    
#     print("-" * (max_word_len + 15))
#     print(f"Total unique words: {len(word_counts)}")

# def main():
#     filename = input("Enter the filename to analyze: ")
    
#     word_counts = count_word_occurrences(filename)
    
#     display_word_counts(word_counts)

# if __name__ == "__main__":
#     main()

"""6) Create a class Student with the attributes such as id, name, address, admission year, level, section. 
Instantiate the object of class to take input for all the attributes and display the output"""

# class Student:
#     def __init__(self, student_id="", name="", address="", admission_year=0, level="", section=""):
#         self.student_id = student_id
#         self.name = name
#         self.address = address
#         self.admission_year = admission_year
#         self.level = level
#         self.section = section
    
#     def input_details(self):
#         print("\nEnter Student Details:")
#         print("-" * 25)
#         self.student_id = input("Enter Student ID: ")
#         self.name = input("Enter Full Name: ")
#         self.address = input("Enter Address: ")
        
#         while True:
#             try:
#                 self.admission_year = int(input("Enter Admission Year: "))
#                 if 1900 <= self.admission_year <= 2100:
#                     break
#                 else:
#                     print("Please enter a valid year between 1900 and 2100.")
#             except ValueError:
#                 print("Please enter a valid year (numeric value).")
        
#         while True:
#             self.level = input("Enter Level: ")
#             if self.level.strip():
#                 break
#             else:
#                 print("Level cannot be empty. Please enter a valid level.")
        
#         while True:
#             self.section = input("Enter Section: ")
#             if self.section.strip():
#                 break
#             else:
#                 print("Section cannot be empty. Please enter a valid section.")
    
#     def display_details(self):
#         print("\nStudent Information:")
#         print("-" * 25)
#         print(f"Student ID: {self.student_id}")
#         print(f"Name: {self.name}")
#         print(f"Address: {self.address}")
#         print(f"Admission Year: {self.admission_year}")
#         print(f"Level: {self.level}")
#         print(f"Section: {self.section}")

# def main():
#     student = Student()
    
#     student.input_details()
   
#     student.display_details()
    
# if __name__ == "__main__":
#     main()

"""7) WAP to implement a class called employee with attributes such as empid, name, address, contact_number, spouse name, number_of_child, salary. 
Instantiate this class to input the values for multiple employees and write it in a file “employees.csv”. 
Allow the user of your program to see the list
of employees and their details as well. Try to use the concept of try/except too in the program. """

# import csv
# import os

# class Employee:
   
#     def __init__(self, empid="", name="", address="", contact_number="", 
#                  spouse_name="", number_of_child=0, salary=0.0):
#         self.empid = empid
#         self.name = name
#         self.address = address
#         self.contact_number = contact_number
#         self.spouse_name = spouse_name
#         self.number_of_child = number_of_child
#         self.salary = salary
    
#     def input_details(self):
#         """
#         Take input from user for all employee attributes with validation.
        
#         Returns:
#             bool: True if input was successful, False otherwise
#         """
#         try:
#             print("\nEnter Employee Details:")
#             print("-" * 25)
#             self.empid = input("Enter Employee ID: ")
#             self.name = input("Enter Full Name: ")
#             self.address = input("Enter Address: ")
            
#             # Validate contact number (simple validation)
#             while True:
#                 self.contact_number = input("Enter Contact Number: ")
#                 if self.contact_number.isdigit() or self.contact_number == "":
#                     break
#                 else:
#                     print("Contact number should contain only digits.")
            
#             self.spouse_name = input("Enter Spouse Name (leave blank if not applicable): ")
            
#             # Validate number of children
#             while True:
#                 try:
#                     child_input = input("Enter Number of Children: ")
#                     self.number_of_child = int(child_input) if child_input else 0
#                     if self.number_of_child >= 0:
#                         break
#                     else:
#                         print("Number of children cannot be negative.")
#                 except ValueError:
#                     print("Please enter a valid number.")
            
#             # Validate salary
#             while True:
#                 try:
#                     salary_input = input("Enter Salary: ")
#                     self.salary = float(salary_input) if salary_input else 0.0
#                     if self.salary >= 0:
#                         break
#                     else:
#                         print("Salary cannot be negative.")
#                 except ValueError:
#                     print("Please enter a valid amount.")
            
#             return True
            
#         except Exception as e:
#             print(f"An error occurred while inputting employee details: {e}")
#             return False
    
#     def to_dict(self):
#         """
#         Convert employee object to dictionary for CSV writing.
        
#         Returns:
#             dict: Dictionary representation of employee attributes
#         """
#         return {
#             'Employee ID': self.empid,
#             'Name': self.name,
#             'Address': self.address,
#             'Contact Number': self.contact_number,
#             'Spouse Name': self.spouse_name,
#             'Number of Children': self.number_of_child,
#             'Salary': self.salary
#         }
    
#     def display(self):
#         """
#         Display employee details.
#         """
#         print(f"ID: {self.empid}, Name: {self.name}, Address: {self.address}")
#         print(f"Contact: {self.contact_number}, Spouse: {self.spouse_name}")
#         print(f"Children: {self.number_of_child}, Salary: ${self.salary:.2f}")


# class EmployeeManager:
#     """
#     A class to manage employees, save to CSV, and display employee data.
    
#     Attributes:
#         filename (str): Name of the CSV file to store employee data
#         employees (list): List of Employee objects
#     """
    
#     def __init__(self, filename="employees.csv"):
#         """
#         Initialize the EmployeeManager with a filename.
        
#         Args:
#             filename (str): Name of the CSV file to store employee data
#         """
#         self.filename = filename
#         self.employees = []
#         self.fieldnames = ['Employee ID', 'Name', 'Address', 'Contact Number', 
#                           'Spouse Name', 'Number of Children', 'Salary']
        
#         # Load existing employees if file exists
#         self.load_employees()
    
#     def load_employees(self):
#         """
#         Load existing employees from CSV file.
#         """
#         try:
#             if os.path.exists(self.filename):
#                 with open(self.filename, 'r', newline='') as file:
#                     reader = csv.DictReader(file)
#                     for row in reader:
#                         emp = Employee(
#                             row['Employee ID'],
#                             row['Name'],
#                             row['Address'],
#                             row['Contact Number'],
#                             row['Spouse Name'],
#                             int(row['Number of Children']),
#                             float(row['Salary'])
#                         )
#                         self.employees.append(emp)
#                 print(f"Loaded {len(self.employees)} employees from file.")
#             else:
#                 print("No existing employee data found. Starting with empty database.")
#         except Exception as e:
#             print(f"Error loading employees: {e}")
    
#     def add_employee(self):
#         """
#         Add a new employee to the list.
        
#         Returns:
#             bool: True if employee was added successfully, False otherwise
#         """
#         try:
#             emp = Employee()
#             if emp.input_details():
#                 self.employees.append(emp)
#                 print("Employee added successfully!")
#                 return True
#             return False
#         except Exception as e:
#             print(f"Error adding employee: {e}")
#             return False
    
#     def save_to_csv(self):
#         """
#         Save all employees to CSV file.
        
#         Returns:
#             bool: True if save was successful, False otherwise
#         """
#         try:
#             with open(self.filename, 'w', newline='') as file:
#                 writer = csv.DictWriter(file, fieldnames=self.fieldnames)
#                 writer.writeheader()
#                 for emp in self.employees:
#                     writer.writerow(emp.to_dict())
#             print(f"Successfully saved {len(self.employees)} employees to {self.filename}")
#             return True
#         except PermissionError:
#             print(f"Permission denied. Cannot write to {self.filename}")
#             return False
#         except Exception as e:
#             print(f"Error saving to CSV: {e}")
#             return False
    
#     def display_all_employees(self):
#         """
#         Display all employees.
#         """
#         if not self.employees:
#             print("No employees to display.")
#             return
        
#         print("\nEmployee List:")
#         print("-" * 50)
#         for i, emp in enumerate(self.employees, 1):
#             print(f"\nEmployee #{i}:")
#             emp.display()
#             print("-" * 50)
    
#     def search_employee(self, empid):
#         """
#         Search for an employee by ID.
        
#         Args:
#             empid (str): Employee ID to search for
            
#         Returns:
#             Employee or None: Employee object if found, None otherwise
#         """
#         for emp in self.employees:
#             if emp.empid == empid:
#                 return emp
#         return None


# def main():
#     # Create an employee manager
#     manager = EmployeeManager()
    
#     while True:
#         try:
#             print("\nEmployee Management System")
#             print("=" * 25)
#             print("1. Add Employee")
#             print("2. Display All Employees")
#             print("3. Search Employee by ID")
#             print("4. Save and Exit")
            
#             choice = input("\nEnter your choice (1-4): ")
            
#             if choice == '1':
#                 manager.add_employee()
#                 # Save after each addition
#                 manager.save_to_csv()
                
#             elif choice == '2':
#                 manager.display_all_employees()
                
#             elif choice == '3':
#                 emp_id = input("Enter Employee ID to search: ")
#                 employee = manager.search_employee(emp_id)
                
#                 if employee:
#                     print("\nEmployee Found:")
#                     print("-" * 25)
#                     employee.display()
#                 else:
#                     print(f"No employee found with ID: {emp_id}")
                    
#             elif choice == '4':
#                 manager.save_to_csv()
#                 print("Exiting program. Goodbye!")
#                 break
                
#             else:
#                 print("Invalid choice. Please enter a number between 1 and 4.")
                
#         except KeyboardInterrupt:
#             print("\nProgram interrupted. Saving data...")
#             manager.save_to_csv()
#             break
            
#         except Exception as e:
#             print(f"An unexpected error occurred: {e}")

# # Execute the main function 
# if __name__ == "__main__":
#     main()

"""8) Write a program to implement a basic library book management with the functionalities such as 
issue the book, return the book and search the book. Use the concept of OOP to create the necessary classes 
on your own and implement the concept of other OOP features. For the storage of book details, 
use the file handling along with the exception handling. """

# import csv
# import os
# from datetime import datetime, timedelta

# class Book:

    
#     def __init__(self, book_id="", title="", author="", publisher="", 
#                  is_available=True, issued_to="", issue_date="", return_date=""):

#         self.book_id = book_id
#         self.title = title
#         self.author = author
#         self.publisher = publisher
#         self.is_available = is_available
#         self.issued_to = issued_to
#         self.issue_date = issue_date
#         self.return_date = return_date
    
#     def display_info(self):

#         status = "Available" if self.is_available else f"Issued to {self.issued_to}"
#         print(f"ID: {self.book_id} | Title: {self.title}")
#         print(f"Author: {self.author} | Publisher: {self.publisher}")
#         print(f"Status: {status}")
        
#         if not self.is_available:
#             print(f"Issue Date: {self.issue_date} | Return Date: {self.return_date}")
    
#     def to_dict(self):
      
#         return {
#             'Book ID': self.book_id,
#             'Title': self.title,
#             'Author': self.author,
#             'Publisher': self.publisher,
#             'Available': str(self.is_available),
#             'Issued To': self.issued_to,
#             'Issue Date': self.issue_date,
#             'Return Date': self.return_date
#         }
    
#     @classmethod
#     def from_dict(cls, data):
     
#         return cls(
#             book_id=data.get('Book ID', ''),
#             title=data.get('Title', ''),
#             author=data.get('Author', ''),
#             publisher=data.get('Publisher', ''),
#             is_available=data.get('Available', 'True').lower() == 'true',
#             issued_to=data.get('Issued To', ''),
#             issue_date=data.get('Issue Date', ''),
#             return_date=data.get('Return Date', '')
#         )


# class Person:
  
#     def __init__(self, person_id="", name="", contact=""):
       
#         self.person_id = person_id
#         self.name = name
#         self.contact = contact
#         self.books_borrowed = []
    
#     def display_info(self):
        
#         print(f"ID: {self.person_id} | Name: {self.name}")
#         print(f"Contact: {self.contact}")
#         print(f"Books Borrowed: {len(self.books_borrowed)}")
    
#     def to_dict(self):
       
#         return {
#             'Person ID': self.person_id,
#             'Name': self.name,
#             'Contact': self.contact,
#             'Books Borrowed': ','.join(self.books_borrowed)
#         }
    
#     @classmethod
#     def from_dict(cls, data):
       
#         person = cls(
#             person_id=data.get('Person ID', ''),
#             name=data.get('Name', ''),
#             contact=data.get('Contact', '')
#         )
#         books_str = data.get('Books Borrowed', '')
#         if books_str:
#             person.books_borrowed = books_str.split(',')
#         return person


# class Library:
   
#     def __init__(self, books_file="books.csv", people_file="borrowers.csv"):
        
#         self.books_file = books_file
#         self.people_file = people_file
#         self.books = {}
#         self.people = {}
        
#         # Load data from files
#         self.load_data()
    
#     def load_data(self):
#         """
#         Load book and people data from CSV files.
#         """
#         # Load books
#         try:
#             if os.path.exists(self.books_file):
#                 with open(self.books_file, 'r', newline='') as file:
#                     reader = csv.DictReader(file)
#                     for row in reader:
#                         book = Book.from_dict(row)
#                         self.books[book.book_id] = book
#                 print(f"Loaded {len(self.books)} books from file.")
#             else:
#                 print("No existing books data found.")
#         except Exception as e:
#             print(f"Error loading books data: {e}")
        
#         # Load people
#         try:
#             if os.path.exists(self.people_file):
#                 with open(self.people_file, 'r', newline='') as file:
#                     reader = csv.DictReader(file)
#                     for row in reader:
#                         person = Person.from_dict(row)
#                         self.people[person.person_id] = person
#                 print(f"Loaded {len(self.people)} borrowers from file.")
#             else:
#                 print("No existing borrowers data found.")
#         except Exception as e:
#             print(f"Error loading borrowers data: {e}")
    
#     def save_data(self):
#         """
#         Save book and people data to CSV files.
#         """
#         # Save books
#         try:
#             with open(self.books_file, 'w', newline='') as file:
#                 fieldnames = ['Book ID', 'Title', 'Author', 'Publisher', 
#                              'Available', 'Issued To', 'Issue Date', 'Return Date']
#                 writer = csv.DictWriter(file, fieldnames=fieldnames)
#                 writer.writeheader()
#                 for book in self.books.values():
#                     writer.writerow(book.to_dict())
#             print(f"Books data saved to {self.books_file}")
#         except Exception as e:
#             print(f"Error saving books data: {e}")
        
#         # Save people
#         try:
#             with open(self.people_file, 'w', newline='') as file:
#                 fieldnames = ['Person ID', 'Name', 'Contact', 'Books Borrowed']
#                 writer = csv.DictWriter(file, fieldnames=fieldnames)
#                 writer.writeheader()
#                 for person in self.people.values():
#                     writer.writerow(person.to_dict())
#             print(f"Borrowers data saved to {self.people_file}")
#         except Exception as e:
#             print(f"Error saving borrowers data: {e}")
    
#     def add_book(self):
#         """
#         Add a new book to the library.
#         """
#         try:
#             print("\nAdd New Book:")
#             print("-" * 20)
            
#             # Input book details
#             book_id = input("Enter Book ID: ")
            
#             # Check if book ID already exists
#             if book_id in self.books:
#                 print("Error: A book with this ID already exists.")
#                 return
                
#             title = input("Enter Title: ")
#             author = input("Enter Author: ")
#             publisher = input("Enter Publisher: ")
            
#             # Create and add the book
#             book = Book(book_id, title, author, publisher)
#             self.books[book_id] = book
            
#             print("Book added successfully!")
            
#         except Exception as e:
#             print(f"Error adding book: {e}")
    
#     def add_borrower(self):
#         """
#         Add a new borrower to the system.
#         """
#         try:
#             print("\nAdd New Borrower:")
#             print("-" * 20)
            
#             # Input borrower details
#             person_id = input("Enter Borrower ID: ")
            
#             # Check if person ID already exists
#             if person_id in self.people:
#                 print("Error: A borrower with this ID already exists.")
#                 return
                
#             name = input("Enter Name: ")
#             contact = input("Enter Contact Information: ")
            
#             # Create and add the borrower
#             person = Person(person_id, name, contact)
#             self.people[person_id] = person
            
#             print("Borrower added successfully!")
            
#         except Exception as e:
#             print(f"Error adding borrower: {e}")
    
#     def issue_book(self):
#         """
#         Issue a book to a borrower.
#         """
#         try:
#             print("\nIssue Book:")
#             print("-" * 20)
            
#             # Get book ID
#             book_id = input("Enter Book ID: ")
#             if book_id not in self.books:
#                 print("Error: Book not found.")
#                 return
                
#             book = self.books[book_id]
#             if not book.is_available:
#                 print(f"Error: Book is already issued to {book.issued_to}.")
#                 return
            
#             # Get borrower ID
#             person_id = input("Enter Borrower ID: ")
#             if person_id not in self.people:
#                 print("Error: Borrower not found.")
#                 return
                
#             person = self.people[person_id]
            
#             # Set issue and return dates
#             issue_date = datetime.now()
#             return_date = issue_date + timedelta(days=14)  # 2 weeks loan period
            
#             # Update book status
#             book.is_available = False
#             book.issued_to = person_id
#             book.issue_date = issue_date.strftime("%Y-%m-%d")
#             book.return_date = return_date.strftime("%Y-%m-%d")
            
#             # Update borrower's borrowed books
#             person.books_borrowed.append(book_id)
            
#             print(f"Book '{book.title}' issued to {person.name} successfully!")
#             print(f"Return Date: {book.return_date}")
            
#         except Exception as e:
#             print(f"Error issuing book: {e}")
    
#     def return_book(self):
#         """
#         Process a book return.
#         """
#         try:
#             print("\nReturn Book:")
#             print("-" * 20)
            
#             # Get book ID
#             book_id = input("Enter Book ID: ")
#             if book_id not in self.books:
#                 print("Error: Book not found.")
#                 return
                
#             book = self.books[book_id]
#             if book.is_available:
#                 print("Error: This book is not currently issued to anyone.")
#                 return
            
#             # Get borrower
#             person_id = book.issued_to
#             if person_id in self.people:
#                 person = self.people[person_id]
                
#                 # Update borrower's borrowed books
#                 if book_id in person.books_borrowed:
#                     person.books_borrowed.remove(book_id)
            
#             # Reset book status
#             book.is_available = True
#             book.issued_to = ""
#             book.issue_date = ""
#             book.return_date = ""
            
#             print(f"Book '{book.title}' returned successfully!")
            
#         except Exception as e:
#             print(f"Error returning book: {e}")
    
#     def search_book(self):
#         """
#         Search for books by various criteria.
#         """
#         try:
#             print("\nSearch Book:")
#             print("-" * 20)
#             print("1. Search by ID")
#             print("2. Search by Title")
#             print("3. Search by Author")
            
#             choice = input("\nEnter your choice (1-3): ")
            
#             results = []
            
#             if choice == '1':
#                 book_id = input("Enter Book ID: ")
#                 if book_id in self.books:
#                     results.append(self.books[book_id])
            
#             elif choice == '2':
#                 title = input("Enter Title (or part of title): ").lower()
#                 for book in self.books.values():
#                     if title in book.title.lower():
#                         results.append(book)
            
#             elif choice == '3':
#                 author = input("Enter Author (or part of author name): ").lower()
#                 for book in self.books.values():
#                     if author in book.author.lower():
#                         results.append(book)
            
#             else:
#                 print("Invalid choice.")
#                 return
            
#             # Display results
#             if results:
#                 print(f"\nFound {len(results)} book(s):")
#                 print("=" * 50)
#                 for i, book in enumerate(results, 1):
#                     print(f"\nBook #{i}:")
#                     book.display_info()
#                     print("-" * 50)
#             else:
#                 print("No books found matching your criteria.")
            
#         except Exception as e:
#             print(f"Error searching books: {e}")
    
#     def display_all_books(self):
#         """
#         Display all books in the library.
#         """
#         if not self.books:
#             print("No books in the library.")
#             return
            
#         try:
#             print("\nAll Books in Library:")
#             print("=" * 50)
#             for i, book in enumerate(self.books.values(), 1):
#                 print(f"\nBook #{i}:")
#                 book.display_info()
#                 print("-" * 50)
                
#         except Exception as e:
#             print(f"Error displaying books: {e}")
    
#     def display_borrowers(self):
#         """
#         Display all borrowers.
#         """
#         if not self.people:
#             print("No borrowers in the system.")
#             return
            
#         try:
#             print("\nAll Borrowers:")
#             print("=" * 50)
#             for i, person in enumerate(self.people.values(), 1):
#                 print(f"\nBorrower #{i}:")
#                 person.display_info()
                
#                 # Display borrowed books
#                 if person.books_borrowed:
#                     print("\nCurrently Borrowed Books:")
#                     for j, book_id in enumerate(person.books_borrowed, 1):
#                         if book_id in self.books:
#                             book = self.books[book_id]
#                             print(f"  {j}. {book.title} (ID: {book.book_id})")
                
#                 print("-" * 50)
                
#         except Exception as e:
#             print(f"Error displaying borrowers: {e}")


# def main():
#     # Create a library system
#     library = Library()
    
#     while True:
#         try:
#             print("\nLibrary Management System")
#             print("=" * 30)
#             print("1. Add New Book")
#             print("2. Add New Borrower")
#             print("3. Issue Book")
#             print("4. Return Book")
#             print("5. Search Book")
#             print("6. Display All Books")
#             print("7. Display All Borrowers")
#             print("8. Save and Exit")
            
#             choice = input("\nEnter your choice (1-8): ")
            
#             if choice == '1':
#                 library.add_book()
#             elif choice == '2':
#                 library.add_borrower()
#             elif choice == '3':
#                 library.issue_book()
#             elif choice == '4':
#                 library.return_book()
#             elif choice == '5':
#                 library.search_book()
#             elif choice == '6':
#                 library.display_all_books()
#             elif choice == '7':
#                 library.display_borrowers()
#             elif choice == '8':
#                 library.save_data()
#                 print("Data saved. Exiting program. Goodbye!")
#                 break
#             else:
#                 print("Invalid choice. Please enter a number between 1 and 8.")
                
#         except KeyboardInterrupt:
#             print("\nProgram interrupted.")
#             choice = input("Save before exiting? (y/n): ")
#             if choice.lower() == 'y':
#                 library.save_data()
#             print("Exiting program. Goodbye!")
#             break
            
#         except Exception as e:
#             print(f"An unexpected error occurred: {e}")

# # Execute the main function when script is run
# if __name__ == "__main__":
#     main()