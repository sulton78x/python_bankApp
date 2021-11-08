# Create a Banking Application that supports creation of New Accounts, Deposit, Withdrawal etc.....

class BankAccount:
    def __init__(self):
        self.balance = 0
        print('\nHello and Thanks for choosing our products....')

    # Make Deposit
    def deposit(self):
        amount = float(input('Enter amount to be deposited : '))
        # add deposit amount to balance
        self.balance += amount
        # Print message
        print('\nAmount Deposited : ', amount)

    # Make Withdrawal
    def withdraw(self):
        amount = float(input('Enter amount to be withdraw : '))
        # Check if 'balance' is greater than 'amount'
        if self.balance >= amount:
            self.balance -= amount
            # Send Debit alert + balance message.
            print('\nAmount Withdrawn', amount)
            print('\nBalance : ', self.balance)

        else:
            print('\nInufficient Funds.')

    # Check Balance
    def checkBalance(self):
        print('\nYour Balance is : ', self.balance)


# Test Code...
newAccount = BankAccount()
newAccount.deposit()
newAccount.withdraw()
newAccount.checkBalance()