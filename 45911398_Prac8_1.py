# 45911398 Prac. 8_1 
# Dante le Roux

def is_palindrome(word):

    # Convert word to lowercase, since python is case sensitive
    word = word.lower()

    # Initialize reversed_word
    reversed_word =""

    # Find the index of the last letter of the word
    index = len(word) -1 

    # Use a while loop to iterate backwards over characters
    while index>= 0:
        # Append characters to reversed word
        reversed_word += word[index]
        # Move index 1 to left to iterate over each word
        index -= 1
   
    # If all corresponding characters match it is a palindrome 
    return word == reversed_word

# Ask user to input a string which is then tested to see if it is a palindrome or not
input_string = input("Enter a string:")

# Check if the input_string is a palindrome, using the palidrome_function
if is_palindrome(input_string):
    # The output if the input_string is a palindrome
    print(f"The '{input_string}' is a palindrome.")
else: 
    # The output if the input_string is NOT a palindrome
    print(f"The '{input_string}' is not a palindrome.")

