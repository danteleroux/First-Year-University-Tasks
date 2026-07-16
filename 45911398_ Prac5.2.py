# 45911398 Dante le Roux
# Creative project

print("""
This is a program designed to calculate the monthly dosage of ahg
certain medication, which has to be tapered by a certain percentage
(given by your doctor), until it has reached a target dosage
(determined by your doctor).
""")

# Asker user to input their original dosage
original_dosage = float(input("Please enter your current medication dosage (mg/day): "))

#  Condition for continuing program
if original_dosage > 0:
    # If true, user may enter their target dosage
    target_dosage = float(input("Please enter what your doctor would like your dosage to be (mg/day): "))

    #  User's target dosage may not be more than the original dosage, as the doctor uses program to taper
    if target_dosage < original_dosage: 

        # User is asked to enter percentage at which decline should happen
        percentage_decline = float(input("Please enter the percentage (%) by which your medication has to decline: "))
        
        # Condition for program to continue 
        if 0< percentage_decline < 10:

            #  Starting at month 0
            print(f"Month 0: {original_dosage} mg/day - Starting dosage.")
            month = 1

            # To allow program to run until target dosage is reached
            while original_dosage > target_dosage:
                original_dosage *= (1 - percentage_decline / 100)

                #  When target dosage is reached it will be printed
                if original_dosage < target_dosage:
                    print(f"Month {month}: {target_dosage} mg/day - Target dosage reached.")
                    break
                else:
                    print(f"Month {month}: {original_dosage:.2f} mg/day")
                month += 1

            #  Informing user what dosage to continue taking, after tapering successfully
            print(f"Final dosage you should continue taking is {int(target_dosage)} mg/day.")
        
        # Output when percentage tapered is incorrecctly entered
        else: 
            print("Your percentage decline cannot be 0, and must be less that 10%, for it to be safe!)")
    
    #  Output when target dosage is bigger than the original dosage
    else:
        print("Your target cannot be bigger than your original dosage")

# Output when original dosage is <= 0
else:
    print("Your original dosage needs to be greater than 0!")



