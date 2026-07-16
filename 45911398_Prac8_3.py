# 45911398_Prac8_3
# Dante le Roux

# Prompting user to input their email address
email = input("Enter your email: ")

# Defining the index of the "@" in the email entered
index_of_at = email.find("@")

# Extracting the username from the email using the position of "@"
username = email[0:index_of_at]

# Extracting the domain from the email, starting right after the "@"
domain = email[index_of_at+1:]

# Printing the results
print(f"Your username is: {username}")
print(f"Your domain is: {domain}")

