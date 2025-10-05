# Example: User Input in Python
# This file demonstrates how to get and use user input

print("=== Personal Information Collector ===\n")

# Get string input
name = input("What is your name? ")
favorite_food = input("What is your favorite food? ")

# Get numeric input (must convert!)
age = int(input("How old are you? "))
height = float(input("What is your height in meters? "))

# Calculate something
years_to_30 = 30 - age
height_in_cm = height * 100

# Display results
print("\n=== Your Profile ===")
print(f"Name: {name}")
print(f"Age: {age} years old")
print(f"Height: {height}m ({height_in_cm}cm)")
print(f"Favorite Food: {favorite_food}")

if age < 30:
    print(f"\nYou will be 30 in {years_to_30} years!")
else:
    print(f"\nYou are {age - 30} years past 30!")

print(f"\nNice to meet you, {name}!")

