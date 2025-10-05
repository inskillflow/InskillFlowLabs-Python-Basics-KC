# Step 4: Practice Challenge

## Time to Put It All Together!

You've learned about variables, data types, and user inputs. Now let's build something real!

---

## Challenge: Student Information System

Create a program that collects and displays student information.

### Requirements:

Your program should:

1. **Ask for:**
   - Student's full name (string)
   - Student's age (integer)
   - Student's GPA (float, 0.0 to 4.0)
   - Whether they're enrolled (boolean - but use input as string)

2. **Calculate:**
   - What year they'll graduate (current year 2025 + 4 years - depends on implementation)

3. **Display:**
   - A nice formatted summary of all information

---

## Starter Template

**Step 1:** Create your challenge file  
`student_system.py`{{open}}

**Step 2:** Use this template:

```python
# Student Information System
print("=== Student Registration System ===\n")

# TODO: Get student's full name


# TODO: Get student's age (convert to integer!)


# TODO: Get student's GPA (convert to float!)


# TODO: Calculate graduation year (current year + 4)


# Display the information
print("\n=== Student Profile ===")
# TODO: Print all the information in a nice format

```

---

## Example Output

Your program should look something like this:

```
=== Student Registration System ===

Enter your full name: Sarah Martinez
Enter your age: 19
Enter your GPA (0.0-4.0): 3.75

=== Student Profile ===
Name: Sarah Martinez
Age: 19 years old
GPA: 3.75
Expected Graduation: 2029

Good luck with your studies, Sarah Martinez!
```

---

## Bonus Challenges

If you finish early, try these enhancements:

### Level 1: Add More Fields
- Student ID number
- Major/Field of study
- Email address

### Level 2: Make It Pretty
- Add decorative lines (========)
- Use emojis
- Color formatting (advanced!)

### Level 3: Calculations
- Calculate years until graduation
- Calculate if GPA is above 3.5 (honor student)
- Calculate age at graduation

---

## Testing Your Program

Run your program multiple times with different inputs:

`python3 student_system.py`{{execute}}

Make sure it works with:
- Short and long names
- Different ages
- Different GPA values (try 4.0, 3.5, 2.8)

---

## Common Issues & Solutions

**Problem:** "invalid literal for int()"  
**Solution:** Make sure you're converting to int() for age

**Problem:** Numbers have too many decimals  
**Solution:** You can use `round(number, 2)` to round to 2 decimals

**Problem:** Want to format GPA to 2 decimal places?  
**Solution:** Use `print(f"GPA: {gpa:.2f}")`

---

## Need Help?

Here's a hint for the full solution structure:

```python
# 1. Get inputs (use input() and convert types)
# 2. Do calculations (graduation year = 2025 + 4)
# 3. Print formatted output (use f-strings or +)
```

Take your time and experiment! Making mistakes is part of learning.

---

When you're done (or if you're stuck), click "Continue" to see a complete solution!

