class BankAccount:
    def __init__(self,account_number,balance):
        self.__account_number = account_number #private attribute
        self.__balance = balance
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            return self.__balance
    def withdrawal(self,amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return self.__balance
    def get_balance(self):
        return self.__balance
    
account = BankAccount("123456789", 1000) #Direct access to private attribute

try:
    account.__balance +=500
except AttributeError :
    print("Cannot access private attribute directly.")
print ("The account balance", account.get_balance())
account.deposit(200)
print ("The account balance after deposit:", account.get_balance())
account.withdrawal (150)
print ("The account balance after withdrawal:", account.get_balance()) 