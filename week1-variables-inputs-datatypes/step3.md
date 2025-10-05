# Step 3: User Inputs

## Making Programs Interactive!

So far, we've been creating variables with fixed values. But what if we want to get information from the user? That's where `input()` comes in!

---

## The input() Function

The `input()` function lets you ask users for information:

```python
variable_name = input("Your question: ")
```

**Important:** `input()` ALWAYS returns a string (text), even if the user types a number!

---

## Your First Interactive Program

**Step 1:** Create a new file  
`interactive.py`{{open}}

**Step 2:** Copy this code:

```python
# Ask for user's name
name = input("What is your name? ")

# Print a personalized greeting
print("Hello, " + name + "! Welcome to Python!")
print("Nice to meet you, " + name)
```

**Step 3:** Run it!  
`python3 interactive.py`{{execute}}

Type your name when prompted and press Enter!

---

## Getting Numbers from Users

Remember: `input()` returns a string. If you need a number, you must convert it!

### Converting Data Types

```python
# Convert string to integer
age = int(input("Enter your age: "))

# Convert string to float
height = float(input("Enter your height in meters: "))
```

**Try this code:**

```python
# Get user's age and calculate birth year
age = int(input("How old are you? "))
current_year = 2025
birth_year = current_year - age

print("You were born in approximately", birth_year)
```

Save it in your file and run:  
`python3 interactive.py`{{execute}}

---

## Common Input Mistakes

### Mistake #1: Forgetting to Convert
```python
# WRONG - Can't do math with strings!
age = input("Age: ")
next_year_age = age + 1  # ERROR!

# RIGHT - Convert first
age = int(input("Age: "))
next_year_age = age + 1  # Works! ✓
```

### Mistake #2: Converting Non-Numbers
```python
# This will crash if user enters text!
age = int(input("Age: "))  # User types "twenty" = ERROR
```

**Solution:** Always tell users what format you expect!

---

## Challenge: Personal Calculator

Create a program that:
1. Asks for two numbers
2. Converts them to floats
3. Adds them together
4. Prints the result

**Example output:**
```
Enter first number: 5.5
Enter second number: 3.2
The sum is: 8.7
```

---

## Multiple Inputs in One Line

You can get several inputs:

```python
name = input("Name: ")
age = input("Age: ")
city = input("City: ")

print(f"{name} is {age} years old and lives in {city}")
```

**Pro Tip:** The `f""` syntax is called an f-string - a modern way to format text!

---

## Key Takeaways

- `input()` gets text from users
- Always returns a string
- Use `int()` to convert to integer
- Use `float()` to convert to decimal
- Tell users what format you expect

Ready for a real challenge? Click "Continue"!

