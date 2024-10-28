#author:MEVIN
#date:28/10/2024
#description     Problem: Write a program that simulates a simple bank ATM system. The user has an initial balance of $1000. The ATM should display a menu with options to:
       # Check Balance
       # Deposit Money
        #Withdraw Money
       # Exit
    #The program should run in a loop until the user chooses to exit. For each option, use if, elif, and else to manage each choice. Ensure that the balance doesn’t go below zero during a withdrawal.
balance_amount=1000
while True:
    print("1.\tCheck Balance")
    print("2.\tDeposit Money")
    print("3.\tWithdraw Money")
    print("4.\tExit")
    choice=int(input("Enter you choice:"))
    if choice==1:
          print(f"The current balance ${balance_amount}")
    elif choice == 2:
        deposit_amount = float(input("Enter the amount"))
        balance_amount = balance_amount +deposit_amount
        print(f"The deposited amount ${deposit_amount} and"f"the current balance ${balance_amount}")
    elif choice==3:
        withdraw_amount = float(input("Enter the amount to withdraw:"))
        balance_amount = balance_amount -withdraw_amount
        print(f"the amount withdrawn from the account"
             f"${withdraw_amount}the balance amount "
        f"${balance_amount}")
    elif choice == 4:
        break
