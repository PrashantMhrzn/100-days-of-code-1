from utils.bank import Bank


def heading():
    print("%"*50)
    print("\t"*2, "BANK MANAGEMENT")
    print("%"*50)


def main():
    heading()
    CHOICE = """1. Create Account
2. Deposit Amount
3. Withdraw Amount
4. Balance Enquiry
5. Holders List
Enter your choice: """
    choice = int(input(CHOICE))
    while choice != 0:
        if choice in range(1, 6):
            if choice == 1:
                account = Bank().create_account()
                print(
                    f"\nAccount created.\nID: {account['id']}\nAmount: {account['amount']}\nDate created: {account['date_created']}\n")
            elif choice == 2:
                acc_id = int(input('Enter account ID: '))
                amount = int(input('Enter amount: '))
                result = Bank(acc_id).deposit_amount(amount)
                print(result)
            elif choice == 3:
                acc_id = int(input('Enter account ID: '))
                amount = int(input('Enter amount: '))
                result = Bank(acc_id).withdraw_amount(amount)
                print(result)
            elif choice == 4:
                acc_id = int(input('Enter account ID:'))
                result = Bank(acc_id).balance_enquiry()
                print(result)
            elif choice == 5:
                Bank().account_list

        else:
            print("Invalid Choice, please choose between 1-5")
        heading()
        choice = int(input(CHOICE))


if __name__ == "__main__":
    main()
