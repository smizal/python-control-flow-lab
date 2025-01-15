# Exercise 0: Example
#
# This is a practice exercise to help you understand how to write code "inside" a provided Python function.
#
# We'll create a function that checks a condition and prints a specific greeting message based on that condition.
#
# Requirements:
# - The function is named `print_greeting`.
# - Inside the function, declare a variable `python_is_fun` and set it to `True`.
# - Use a conditional statement to check if `python_is_fun` is `True`.
# - If `python_is_fun` is `True`, print the message "Python is fun!"

def print_greeting():
    # Your code goes here. Remember to indent!
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

# Call the function
print_greeting()


# ---------------------------------------------------
# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.
print('\n')
print('--- Exercise 1: Vowel or Consonant')
def check_letter():
    # Your control flow logic goes here
    letter = input('Enter a letter (a-z or A-Z) : ').lower()
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        print(f'The letter {letter} is a vowel.')
    else:
        print(f'The letter {letter} is a consonant.')
# Call the function
check_letter()


# ------------------------------------------------------------
# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.
print('\n')
print('--- Exercise 2: Old enough to vote?')
def check_voting_eligibility():
    # Your control flow logic goes here
    age = input('Please enter your age: ')
    try:
        age = int(age)
        if age > 19:
            print('You are eligible to vote based on the entered age')
        else:
            print('You are not eligible to vote based on the entered age')
    except ValueError:
        print('Error: not a valid age number')
# Call the function
check_voting_eligibility()

# -----------------------------------------------------------
# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.
print('\n')
print('--- Exercise 3: Calculate Dog Years')
def calculate_dog_years():
    # Your control flow logic goes here
    age = input("Input a dog's age: ")
    try:
        age = int(age)
        if age == 1 or age ==2:
            dog_age = age * 10
        else:
            dog_age = (2 * 10) + ((age-2) * 7)
        print(f"The dog's age in dog years is {dog_age}")
    except ValueError:
        print('Error: not a valid age number')
# Call the function
calculate_dog_years()

# -----------------------------------

# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.
print('\n')
print('--- Exercise 4: Weather Advice')
def weather_advice():
    # Your control flow logic goes here
    cold = input('is it cold? (yes/no) : ')
    raining = input('is it raining? (yes/no) : ')
    if cold == 'yes' and raining == 'yes':
        print("Wear a waterproof coat.")
    elif cold == 'yes' and raining == 'no':
        print("Wear a warm coat.")
    elif cold == 'no' and raining == 'yes':
        print("Carry an umbrella.")
    else:
        print("Wear light clothing.")
# Call the function
weather_advice()


# -----------------------------------------------------
# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.
print('\n')
print("--- Exercise 5: What's the Season?")
def determine_season():
    # Your control flow logic goes here
    month = input("Enter the month of the year (Jan - Dec): ").lower()
    day = input("Enter the day of the month:" )
    try:
        day = int(day)
        season = ''
        if day >=1 and day <=31:
            if month == 'dec' and day >=21 or month=="jan" or month=="feb" or month=="mar" and day <=19:
                season = 'Winter'
            elif month == 'mar' and day >=20 or month=="apr" or month=="may" or month=="jun" and day <=20:
                season = 'Spring'
            elif month == 'jun' and day >=21 or month=="jul" or month=="aug" or month=="sep" and day <=21:
                season = 'Summer'
            elif month == 'sep' and day >=22 or month=="oct" or month=="nov" or month=="dec" and day <=20:
                season = 'Fall'
        
        if season:
            print(f"{str.capitalize(month)} {str(day)} is in {season}.")
        else:
            print('Not a valid data')
    except ValueError:
        print('Error: not a valid age number')
# Call the function
determine_season()

# ------------------------------------------------------------
# Exercise 7: Number Guessing Game
#
# Write a Python function named `guess_number` that allows a user to guess a predetermined number within a range.
#
# Requirements:
# - Set a fixed number as the target for guessing (e.g., 42).
# - Prompt the user to guess a number within a range (e.g., 1 to 100).
# - Allow the user to guess up to five times.
# - After each guess, use conditional statements with AND, OR, and NOT to give the user hints like:
#   - "Guess is too low" or "Guess is too high."
#   - "Last chance!" when they are on their fifth guess.
# - Print "Congratulations, you guessed correctly!" if they guess the number.
# - Print "Sorry, you failed to guess the number in five attempts." if they do not succeed.
#
# Hints:
# - Use a for loop with a range to limit guesses to five.
# - Use logical AND, OR, and NOT to check conditions and provide appropriate feedback.
print('\n')
print("--- Exercise 7: Number Guessing Game")
def guess_number():
    # Your control flow logic goes here
    TARGET = 42
    attempt = 1
    success = False
    while attempt <= 5:
        if attempt == 5:
            print("Last chance!")
        number = input('guess a number within a range (1 to 100) : ')
        try:
            number = int(number)
            if number < TARGET:
                print("Guess is low")
            elif number > TARGET:
                print("Guess is high")
            else:
                success = True
                break
        except ValueError:
            print('Error: not a valid number')
        attempt += 1
    if success:
        print('Congratulations, you guessed correctly!')
    else:
        print('Sorry, you failed to guess the number in five attempts.')
# Call the function
guess_number()


