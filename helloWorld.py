# Palindrome is a word that reads the same word backward as it does forward.
# For an example bob, nan & mom.

user_input = input("Please enter a name : ")
user_input = user_input.lower() # Make the output to be in lowercase.
reverse = user_input[::-1] # Reverse the word stored in backward.

# The 2 variables are equal.
# Display message will be saying that "the word the user input is a palindrome."
# else the display message will say that "the word the user input is not a palindrome."

if user_input == reverse:
    print(" The word the user input is a Palindrome.")
else:
    print(" The word the user input is not a Palindrome.")