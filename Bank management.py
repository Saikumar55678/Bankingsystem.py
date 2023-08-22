print("=============================================")

customernames = ["saikumar", "aravind", "keerthi"]
customerpins = ["2345", "1234", "6789"]
customerbalance = [10000, 20000, 30000]
deposition = 0
withdrawal = 0
balance = 0
counter_1 = 1
counter_2 = 5
i = 0

while True:
    # os.system('cls')
    print("=====================================")
    print("  ---Welcome to Mahal Bank-----        ")
    print("  ************************************  ")
    print("=<< 1.Open a new account    >>=")
    print("=<< 2.withdraw money >>=")
    print("=<< 3.Deposit Money >>=")
    print("=>> 4.Check Customers & Balance>>==")
    print("=>> 5.Exit >>==")
    print("****************************************")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        new_name = input("Enter your name: ")
        new_pin = input("Enter a 4-digit PIN: ")
        customernames.append(new_name)
        customerpins.append(new_pin)
        customerbalance.append(0)
        print("Account created successfully!")

    elif choice == 2:
        pin = input("Enter your PIN: ")
        index = customerpins.index(pin)
        withdrawal = float(input("Enter the amount to withdraw: "))
        if customerbalance[index] >= withdrawal:
            customerbalance[index] -= withdrawal
            print("Withdrawal successful. Remaining balance:", customerbalance[index])
        else:
            print("Insufficient balance!")

    elif choice == 3:
        pin = input("Enter your PIN: ")
        index = customerpins.index(pin)
        deposition = float(input("Enter the amount to deposit: "))
        customerbalance[index] += deposition
        print("Deposit successful. Updated balance:", customerbalance[index])

    elif choice == 4:
        print("Customer List and Balances:")
        for i in range(len(customernames)):
            print(f"Customer Name: {customernames[i]}, Balance: {customerbalance[i]}")

    elif choice == 5:
        print("Thank you for using Mahal Bank!")
        break

    else:
        print("Invalid choice! Please choose a valid option.")
