#  Format of age
age = 00

# Input user age
age = int(input("Enter you age: "))

# Categories according to user age
if age <= 1:
    print("You're an infant")
elif 2 <= age <=12:
    print("You're a Child")
elif 13 <= age <= 19:
    print ("You're a Teenager")
elif 20 <= age <= 64:
    print ("You're an Adult")
elif age >= 65:
    print ("You're a Senior")



