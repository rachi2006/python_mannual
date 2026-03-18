class customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name

    def display_customer(self):
        print(f"customer_id : {self.customer_id} and name : {self.name}")

class Account:
    def __init__(self, account_number, customer, balance=0):
        self.account_number = account_number
        self.customer = customer
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount} is deposited")
        else:
            print("invalide entered")

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -=amount
            print(f"${amount} is withdrawed")
        else:
            print("insafficent balance. enter valid amount")

    def display_account(self):
        print(f"account no:{self.account_number}, balance : {self.balance}")
        self.customer.display_customer()
    

class bank:
    def __init__(self, bank_name, ):
        self.bank_name = bank_name
        self.accountLi = [] 

    def add_account(self, account):
        self.accountLi.append(account)  

    def display_detailsofBank(self):
        print(f"account in {self.bank_name}")
        for acc in self.accountLi:
            acc.display_account() 
            print("-" *30)



cus1 = customer(121, "rachith")
acc1 = Account(121345, cus1, 21)
acc1.deposit(2000000)
acc1.withdraw(1000000)
bank = bank("sbi")
bank.display_detailsofBank()
acc1.display_account()

                          