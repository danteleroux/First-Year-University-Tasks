# 45911398 Dante le Roux
# Prac6_2

# Printing bank's name
print("NWU BANK")

# Asking user for password
password = int(input("Enter your password (Divisible by 125): "))

# Condition for password
while password % 125!=0:
    password = int(input("Enter your password (Divisible by 125): "))

# Notifying user that login was successful
print("Login Successful!")

# Asking user for their name and initial balance
name = input("Enter your name: ")
in_bal = int(input("Enter initial balance: R "))    

# Printing user's input
print("Account created succesfully!")

# Initialize current balance with the int balance 
current_bal = float(in_bal)

#  Choices that users can choose from
while True:
    one = print("1. Deposit")
    two = print("2. Withdraw")
    three = print("3. Check Balance")
    four = print("4. Exit")

# Asking user to input their choice
    choice = int(input("Enter your choice: "))

 # Running program according to choice
    #  Choice 1
    if choice == 1:
        depo = float(input("Enter amount to deposit: R "))
        current_bal += depo
        ans = print(f"Deposited R{depo:.2f}. Current balance: R{current_bal:.2f}")
    
    # Choice 2
    elif choice == 2:
        withdraw = float(input("Enter amount to withdraw: R "))
        if withdraw <= current_bal:
            current_bal -= withdraw
            wthdrw = print(f"Withdrew R{withdraw:.2f}. Current balance: R{current_bal:.2f} ")
        else:
             print("Insufficient funds.")

    # Choice 3
    elif choice == 3:
            check_bal = print(f"Current balance for {name}: R{current_bal:.2f}")
    
    # Choice 4
    elif choice == 4: 
        print("Exiting...")
        break   
   
    # If user chooses anything other than choices listed
    else:
         print("Invalid choice. Please choose a valid option (1-4).")
