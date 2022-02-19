accounts = ["A0123"]

def isAccountExists(accountNum):
    for account in accounts:
        if account == accountNum:
            return True
    return False

def showMenuOptions():
    print("'d':  Deposit Amount")
    print("'t':  Show all transactions")
    print("'w':  Withdraw amoount")
    print("'e':  End application")
    action = input("Enter your option, please: ")
    print(str(action))
    if str(action) == "e":
        exit()

def initiateApp():
    accountNumber = input("Enter account number: ")
    if not isAccountExists(str(accountNumber)):
        print("Creating new account")
        accountNumber = input("Enter account number: ")
        accounts.append(str(accountNumber))
        print(accounts)
        if str(accountNumber):
            showMenuOptions()

initiateApp()