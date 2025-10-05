# Step 2: Data Types in Python

## What are Data Types?

Data types define what kind of data a variable can hold. Python has several built-in data types, and today we'll learn the most important ones!

---

## The Four Essential Data Types

### 1. **String (str)** - Text
Text enclosed in quotes (single or double)
```python
name = "Alice"
message = 'Hello World'
```

### 2. **Integer (int)** - Whole Numbers
Numbers without decimals
```python
age = 25
year = 2025
```

### 3. **Float** - Decimal Numbers
Numbers with decimal points
```python
price = 19.99
temperature = 36.6
```

### 4. **Boolean (bool)** - True/False
True or False values (note the capital letters!)
```python
is_student = True
is_raining = False
```

---

## Let's Explore Data Types

**Step 1:** Open a new file  
`datatypes.py`{{open}}

**Step 2:** Copy this code:

```python
# String - text data
student_name = "Alex Johnson"
favorite_language = "Python"

# Integer - whole numbers
student_age = 20
students_in_class = 30

# Float - decimal numbers
gpa = 3.85
course_price = 99.99

# Boolean - True or False
is_enrolled = True
has_completed_course = False

# Print everything
print("Name:", student_name)
print("Age:", student_age)
print("GPA:", gpa)
print("Enrolled:", is_enrolled)
```

**Step 3:** Run the code  
`python3 datatypes.py`{{execute}}

---

## Check Data Types

Python has a built-in function to check data types: `type()`

**Add this to your file:**

```python
# Check the type of variables
print("\nData Types:")
print(type(student_name))    # <class 'str'>
print(type(student_age))     # <class 'int'>
print(type(gpa))             # <class 'float'>
print(type(is_enrolled))     # <class 'bool'>
```

Run it again:  
`python3 datatypes.py`{{execute}}

---

## Challenge: Create Your Profile

Create variables for yourself:
- Your name (string)
- Your age (integer)
- Your height in meters (float)
- Whether you like programming (boolean)

Print all of them!

---

## Key Takeaways

- **Strings** = Text in quotes
- **Integers** = Whole numbers
- **Floats** = Decimal numbers
- **Booleans** = True or False

**Important:** Numbers in quotes become strings!
```python
age = 25        # This is an integer
age = "25"      # This is a string!
```

Ready for user input? Click "Continue"!

