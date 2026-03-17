# balance=0

# def main():
#     print("Balance :", balance)
#     deposit()
#     withdraw()
#     print("Balance :", balance)

# def deposit():
#     global balance
#     dep=int(input("Enter deposit :"))
#     balance += dep

# def withdraw():
#     global balance
#     wt=int(input("Enter withdraw :"))
#     balance -= wt


# if __name__=="__main__":
#     main()

## Using Classes :
class Account:
    def __init__(self):
        self._balance=0

    @property
    def balance(self):
        return self._balance
    
    def deposit(self, n):
        self._balance +=n

    def withdraw(self, n):
        self._balance -=n

def main():
    account=Account()
    print("Balance : ", account.balance)
    account.deposit(100)
    print("Balance : ", account.balance)
    account.withdraw(20)
    print("Balance : ", account.balance)

if __name__=="__main__":
    main()