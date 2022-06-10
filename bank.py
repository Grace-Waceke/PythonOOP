class Account:
    def __init__(self, name, number):
        self.name = name
        self.number =  number
        self.balance = 0
        self.deposits = []
        self.withdrawals = []

    def deposit(self,amount):
        if amount<=0:
            return f"Deposit amount must be greater than zero"
        else:
            self.balance += amount
            self.deposits.append(amount)
            return f" Hello {self.name}, you have deposited {amount}, your new balance is {self.balance},{self.deposits}"
            # Conditions for withdrawal to be successful;
            # Requested amount must be greater than amount balance and greater than zero too

    def withdrawal(self,amount):
        self.transactions = 100
        if amount <=0:
            return f"withdraw should be positive"
        elif amount > self.balance:
            return f"Your balance is {self.balance} and you cannot withdraw {amount}"
        else:
            self.balance -= amount+self.transactions
            self.withdrawals.append(amount)
            return f"you have withdrawn {amount} and your balance is {self.balance}, the transaction fee is {self.transactions}, and your your total withdrawal is {self.withdrawals}"

    def deposits_statement(self):
        for x in self.deposits:
            print(x,end="\n")

    def withdrawals_statement(self):
        for y in self.deposits:
            print(y,end="\n")

    def current_balance(self):
        return f"{self.balance}"
            

    


