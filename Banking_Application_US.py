class BankAccount_US:
    def __init__(self,transit_number,account_number,balance):
        self.__transit_number = transit_number  # private attribute
        self.__account_number = account_number  # private attribute
        self.__balance = balance  # private attribute
        transit_number = int(input("Enter the transit number (5 digits): "))
        if len(str(transit_number)) != 5:
            raise ValueError("Invalid transit number. It must be 5 digits.")
        else:
            print (f"Transit Number: {transit_number}")