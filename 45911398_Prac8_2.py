# 45911398_Prac8_2
# Dante le Roux

# Defining a string that contains all vowels (upper- and lowercase)
vowels = "aeiouAEIOU"

# Prompt user to enter a sentence which will be used
ent_sen = input("Please enter a sentence: ")

# Initializing an empty string to accumulate the vowels
vowels_removed = ""

# For loop to iterate over each character
for ch in ent_sen:
    # Check if the current character is NOT a vowel
    if ch not in vowels:
        # If it's not a vowel, it will be added to the vowels_removed string
        vowels_removed += ch

# Print sentence without the vowels
print(vowels_removed)


