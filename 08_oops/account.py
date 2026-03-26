class Account:
    def __init__(self, acc_no, acc_balance, acc_pass):
        self.acc_no = acc_no
        self.acc_balance = acc_balance
        self.__acc_pass = acc_pass # __ before field name makes it work like private that is accessible inside class only

    def debit(self, amount):
        if amount > self.acc_balance:
            return "Not enough amount"
        self.acc_balance = self.acc_balance - amount
        return f"amount deducted {self.acc_balance} remaining"
    

    def credit(self, amount):
        self.acc_balance += amount
        return f"amount added {self.acc_balance} is new balance"
    
    def view_balance(self):
        return self.acc_balance
    
acc1 = Account("123", 10000000, "abc123@")

print(acc1.debit(10000))

print(acc1.credit(100000))

print(acc1.view_balance())
