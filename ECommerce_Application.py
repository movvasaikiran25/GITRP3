class Users:
    def __init__(self,cart,transaction_total):
        self.__cart = cart  # private attribute
        self.__transaction_total = transaction_total
        cart_input = input("Enter the cart items (comma separated): ")
        cart_list = [item.strip() for item in cart_input.split(",")]
        for item in cart_list:
           if item in ["colorbar","maybelline","lakme"] :
            continue
           print (f"Cart Item: {item}")
        else:
            print("No valid cart items found.")
    def successful_transaction(self,Bank,amount):
        if Bank in ["sbi","icici","idfc"] and amount >0 :
            self.__transaction_total += amount
            return self.__transaction_total
    def failed_transaction(self,Bank,amount):
        if Bank not in ["sbi","icici","idfc"] or amount is None :
            return "Transaction failed due to invalid UPI or amount."
    def get_transaction_total(self):
        return self.__transaction_total
    
user = Users(["colorbar","maybelline","lakme"], 250)
    

try:
        user.__transaction_total +=5000
except AttributeError :
        print("Cannot access private attribute directly.")

print ("The transaction total", user.get_transaction_total())
user.successful_transaction ("sbi",300)
print ("The transaction total after successful transaction:", user.get_transaction_total())
user.failed_transaction ("hdfc",None)
print ("The transaction total after failed transaction:", user.get_transaction_total())