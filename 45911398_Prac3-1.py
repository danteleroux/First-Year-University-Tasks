# Number input
num = int(input("Enter a number: "))

# Categories of number
def check_number(num):
    if num > 0:
        return "The number is Positive"
    elif num < 0:
        return "The number is Negative"
    else:
        return "The number is Zero"

# Result of category of number
result = check_number(num)
print(result)