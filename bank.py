class Bank:
        def __init__(self,account_name,account_pin,account_number,account_balance, amount):
            self.account_name=account_name
            self.account_pin=account_pin
            self.account_number=account_number
            self.account_balance=account_balance
            self.amount=amount
        
        def deposit(self):
            self.account_balance+=self.amount
            return self.account_balance
            
        def withdraw(self):
            self.account_balance-=self.amount
            return self.account_balance



