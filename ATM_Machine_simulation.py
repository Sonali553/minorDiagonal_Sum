class InsufficientFundsException(Exception):
    pass
class InvalidAmountException(Exception):
    pass
class ATM_Functionalities:
    def __init__(self):
        self.__balance = 10000
    def balance_Money(self):
        return (self.__balance)
    def withdraw_Money(self,withdraw):
        try:
            if withdraw > self.__balance:
                raise InsufficientFundsException
            elif withdraw <= 0:
                raise InvalidAmountException

            
            else:
                self.__balance -= withdraw
                return (self.__balance)
            
        except InsufficientFundsException:
                print("Balance Insufficient")
        except InvalidAmountException:
            print("Invalid amount, Enter valid amount")
    def deposit(self,deposit):
        self.deposit=deposit
        self.__balance+=deposit
        return (self.__balance)

    def main_function(self):
        
           
            m = 0
            while(m != 1):
             print("Enter your choices")
             print("Enter 1 for withdraw amount")
             print("Enter 2 for Deposit amount")
             print("Enter 3 for Balance Enquiry")
             print("Enter 4 for Exit")
             choice=int(input("Enter your choice: "))
             if choice == 1:
                withdraw=int(input("Enter the amount to be withdraw:"))
                print("After withdraw your balance is",self.withdraw_Money(withdraw))
                
            
             elif choice == 2:
                deposit=int(input("Enter the amount to be deposited:"))
                print("After the deposit your balnce is",self.deposit(deposit))
            
             elif choice == 3:
              print("your balance is",self.balance())
           
             elif choice == 4:
                print("Thank you!")
                m = 1
             else:
                print("Invalid choice")
        
ATM = ATM_Functionalities()
ATM.main_function()


