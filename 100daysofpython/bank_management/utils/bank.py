import datetime


class Bank:
    ACCOUNTS = [
        {"id": 1,
         "amount": 0,
         "date_created": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
         }
    ]

    def __init__(self, account_id=None):
        self.account_id = account_id

    def create_account(self):
        account = {
            'id': len(self.ACCOUNTS) + 1,
            'amount': 0,
            'date_created': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.ACCOUNTS.append(account)
        return account

    def deposit_amount(self, amount):
        for account in self.ACCOUNTS:
            if account['id'] == self.account_id:
                account['amount'] += amount
                return(f'Rs {amount} deposited to account id {self.account_id}')
        return f"Account with id {self.account_id} was not found."

    def withdraw_amount(self, amount):
        for account in self.ACCOUNTS:
            if account['id'] == self.account_id and account['amount'] > amount:
                account['amount'] -= amount
                return(
                    f'Rs {amount} was withdrawn from account id {self.account_id}')
        return f"Account with id {self.account_id} was not found."

    def balance_enquiry(self):
        for account in self.ACCOUNTS:
            if account['id'] == self.account_id:
                return(
                    f"ID: {account['id']}\nAmount: {account['amount']}\nDate created: {account['date_created']}\n")

    @property
    def account_list(self):
        for account in self.ACCOUNTS:
            print(
                f"ID: {account['id']}\nAmount: {account['amount']}\nDate created: {account['date_created']}\n")
