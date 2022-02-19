import datetime
from os import path

accounts = []
timeNow = datetime.datetime.now()

def isAccountExists(accountNum):
    for account in accounts:
        if account['account_num'] == accountNum:
            return True
    return False

def showMenuOptions():
    isCorrectOption = False
    while not isCorrectOption:
        print("'d':  Deposit Amount")
        print("'t':  Show all transactions")
        print("'w':  Withdraw amoount")
        print("'e':  End application")
        action = input("Enter your option, please: ")
        if str(action) == 'd' or str(action) == 't' or str(action) == 'w' or str(action) == 'e':
            isCorrectOption = True
            return str(action)
        else:
            print("Enter valid choice, 'd', 't', 'w' or 'e'....")

def depositMoney(accFile):
    amount = input("Enter amount to deposit:  $")
    if float(amount) > 0:
        for account in accounts:
            if account['account_num'] == accFile[:-4]:
                newBal = float(account['transactions'][-1]['balance'][1:]) + float(amoount)
                newDeposit = {
                    'trans_type': 'deposit amount',
                    'trans_time': str(timeNow.strftime("%d")) + "-" + str(timeNow.strftime("%m")) + "-" + str(timeNow.strftime("%Y")) + " at " + str(timeNow.strftime("%X")),
                    'prev_bal': '$' + str(account['transactions'][-1]['balance']),
                    'trans_amount': '$' + str(float(amoount)),
                    'balance': '$' + str(newBal)
                }
                account['transactions'].append(newDeposit)
                updateAcc = open(accFile, "a")
                updateAcc.write('Transaction type  ' + '  Trans. completed on  ' + '  Previous Balance  ' + '  Trans. Amount  ' + '  Balance  \n')
                updateAcc.write(newDeposit['trans_type'] + '      ' + newDeposit['trans_time'] + '        ' + newDeposit['prev_bal'] + '               ' + newDeposit['trans_amount'] + '          ' + newDeposit['balance'] + '\n')
                updateAcc.close()
                print("Balance before deposit is:  " + account['transactions'][-1]['balance'])
                print("                                     Deposit transaction completed....")
    else:
        print('Invalid amount!')
                    

def showTransactions(accFile):
    if accFile:
        readAccData = open(accFile, 'r')
        print('Transaction Details')
        print(readAccData.read())
        print('End of All Transactions...')


def initiateApp():
    accountNumber = input("Enter account number: ")
    fileName = str(accountNumber) + ".dat"
    if not isAccountExists(str(accountNumber)) and not path.exists(fileName):
        print("Creating new account")
        newAccNumber = input("Enter account number: ")
        accOpenData = {
            'account_num': str(newAccNumber),
            'transactions': [
                {
                    'trans_type': 'open account',
                    'trans_time': str(timeNow.strftime("%d")) + "-" + str(timeNow.strftime("%m")) + "-" + str(timeNow.strftime("%Y")) + " at " + str(timeNow.strftime("%X")),
                    'prev_bal': '$' + str(0.00),
                    'trans_amount': '$' + str(0.00),
                    'balance': '$' + str(0.00)
                }
            ]
        }
        accounts.append(accOpenData)
        accFile = open(fileName, "a")
        accFile.write('Account Number:  ' + accOpenData['account_num'] + '\n')
        accFile.write('Transaction type  ' + '  Trans. completed on  ' + '  Previous Balance  ' + '  Trans. Amount  ' + '  Balance  \n')
        accFile.write(accOpenData['transactions'][0]['trans_type'] + '      ' + accOpenData['transactions'][0]['trans_time'] + '        ' + accOpenData['transactions'][0]['prev_bal'] + '               ' + accOpenData['transactions'][0]['trans_amount'] + '          ' + accOpenData['transactions'][0]['balance'] + '\n')
        accFile.close()
        option = showMenuOptions()
        if option == 'd':
            depositMoney(fileName)
        elif option == 't':
            showTransactions(fileName)
        else:
            print("Closing account and all transactions")
    else:
        option = showMenuOptions()
        if option == 'd':
            depositMoney(fileName)
        elif option == 't':
            showTransactions(fileName)
        else:
            print("Closing account and all transactions")
    print(accounts)


initiateApp()