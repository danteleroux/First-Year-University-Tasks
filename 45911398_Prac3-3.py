# Name of programme
print("Triangle Type Checker")

# Does user want to continue with programme
con_going = "1 (Yes)"
con_going = input("Do you want to keep continue? 1 (Yes) or 2 (No) : ")

# Asking for lengths of sides of triangle
while con_going == "1":
    for i in range (1):
        a = int((input("Enter length of side A: ")))
        b = int((input("Enter length of side B: ")))
        c = int((input("Enter length of side C: ")))
    
# Printing types of triangles   
    if a == b == c :
        print("Equiliteral triangle")
    elif a == b or b == c or c == a:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")


