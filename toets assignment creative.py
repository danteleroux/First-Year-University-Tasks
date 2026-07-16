# 45911398 Dante le Roux
# Creative project

print("This is program designed to calculate the dosage of sleep medication, which has to decline by 10%, until it has reached 50% of your original dosage. ")

original_dosage = float(input("Please enter your current sleep medication dosage (mg /day): "))
target_dosage_factor = 0.5 
target_dosage = target_dosage_factor * original_dosage
percentage_decline = float(input("Please enter the percentage(%) by which your medication has to decline: "))

if original_dosage > 0:
    month_0 = print(f"Month 0: {original_dosage} mg /day - Starting dosage.")

# We start counting from month 1
# month =1 

# The calculations
    for month in range(1, 1000):
        original_dosage *= (1- percentage_decline/100)
        if original_dosage <= target_dosage:
            original_dosage = target_dosage
            print(f"Month {month}: {original_dosage: .2f} mg /day- Target dosage reached")
            break
        else:
            print(f"Month {month}: {original_dosage: .2f} mg /day")
    print(f"Final dosage you should continue taking: {target_dosage:.2f} mg, daily")
else:
    print("Your original dosage needs to be greater that 0!")
