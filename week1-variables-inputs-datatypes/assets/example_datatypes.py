# Example: Data Types in Python
# This file shows the main data types you'll use

# String - text data
student_name = "Alex Johnson"
favorite_color = "Blue"

# Integer - whole numbers
age = 20
year = 2025

# Float - decimal numbers
height = 1.75
gpa = 3.85

# Boolean - True or False
is_student = True
graduated = False

# Print all variables
print("=== Student Information ===")
print("Name:", student_name)
print("Age:", age)
print("Height:", height, "meters")
print("GPA:", gpa)
print("Is Student:", is_student)
print("Graduated:", graduated)

# Check data types
print("\n=== Data Types ===")
print("Type of name:", type(student_name))
print("Type of age:", type(age))
print("Type of height:", type(height))
print("Type of is_student:", type(is_student))

# Important: Numbers in quotes are strings!
age_as_string = "20"
print("\n=== Comparison ===")
print("age:", age, "- Type:", type(age))
print("age_as_string:", age_as_string, "- Type:", type(age_as_string))

