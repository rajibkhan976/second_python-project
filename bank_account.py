import datetime
from os import path

timeNow = datetime.datetime.now()

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

def retrieveAccData(accFile):
    accData = []
    item = {}
    fields = ['trans_type', 'trans_time', 'prev_bal', 'trans_amount', 'balance']
    with open(accFile) as fileDb:
        for row in fileDb:
            data = row.strip().split(', ', len(fields))
            i = 0
            while i < len(fields):
                item[fields[i]] = data[i]
                i += 1
                if len(fields) - i == 1:
                    accData.append(item)
    return accData

def depositAmount(accFile):
    amount = input("Enter amount to deposit:  $")
    if float(amount) > 0:
        if path.exists(accFile):
                accData = retrieveAccData(accFile)
                newBalance = float(accData[-1]['balance'][1:]) + float(amount)
                newDeposit = {
                    'trans_type': "deposit amount",
                    'trans_time': str(timeNow.strftime("%d")) + "-" + str(timeNow.strftime("%m")) + "-" + str(timeNow.strftime("%Y")) + " at " + str(timeNow.strftime("%X")),
                    'prev_bal': '$' + str(accData[-1]['balance'][1:]),
                    'trans_amount': '$' + str(float(amount)),
                    'balance': '$' + str(newBalance)
                }
                updateAcc = open(accFile, "a")
                updateAcc.write(newDeposit['trans_type'] + ", " + newDeposit['trans_time'] + ", " + newDeposit['prev_bal'] + ", " + newDeposit['trans_amount'] + ", " + newDeposit['balance'] + '\n')
                updateAcc.close()
                print("Balance before deposit is:  " + accData[-1]['balance'])
                print("Deposit transaction completed....")
            
    else:
        print('Invalid amount!')
                    
def displayTransactions(accFile):
    if path.exists(accFile):
        print('Transaction Details')
        print('Account Number:  ' + accFile[:-4])
        print('Transaction type' + ', ' + 'Trans. completed on' + ', ' + 'Previous Balance' + ', ' + 'Trans. Amount' + ', ' + 'Balance' + '\n')
        readAccData = open(accFile, 'r')
        print(readAccData.read())
        print('End of All Transactions...')

def withdrawAmount(accFile):
    amount = input("Enter amount to withdraw:  $")
    if float(amount) > 0:
        if path.exists(accFile):
                accData = retrieveAccData(accFile)
                print("Amount balance before withdrawing the amount:  " + accData[-1]['balance'])
                if float(amount) > float(accData[-1]['balance'][1:]):
                    print('Not Sufficient funds in account.')
                    print('$' + str(float(amount)) + ' is higher than amount in account...')
                    print("... transaction completed....")
                else:
                    newBalance = float(accData[-1]['balance'][1:]) - float(amount)
                    newDeposit = {
                        'trans_type': "withdraw amount",
                        'trans_time': str(timeNow.strftime("%d")) + "-" + str(timeNow.strftime("%m")) + "-" + str(timeNow.strftime("%Y")) + " at " + str(timeNow.strftime("%X")),
                        'prev_bal': '$' + str(accData[-1]['balance'][1:]),
                        'trans_amount': '$' + str(float(amount)),
                        'balance': '$' + str(newBalance)
                    }
                    updateAcc = open(accFile, "a")
                    updateAcc.write(newDeposit['trans_type'] + ", " + newDeposit['trans_time'] + ", " + newDeposit['prev_bal'] + ", " + newDeposit['trans_amount'] + ", " + newDeposit['balance'] + '\n')
                    updateAcc.close()
                    print("... transaction completed....")
    else:
        print('Invalid amount!')


def initiateApp():
    accountNumber = input("Enter account number: ")
    fileName = str(accountNumber) + ".dat"
    if not path.exists(fileName):
        print("Creating new account")
        newAccNumber = input("Enter account number: ")
        accOpenData = {
            'trans_type': "open account",
            'trans_time': str(timeNow.strftime("%d")) + "-" + str(timeNow.strftime("%m")) + "-" + str(timeNow.strftime("%Y")) + " at " + str(timeNow.strftime("%X")),
            'prev_bal': '$' + str(0.00),
            'trans_amount': '$' + str(0.00),
            'balance': '$' + str(0.00)
        }
        fileName =  str(newAccNumber) + ".dat"
        accFile = open(fileName, "a")
        accFile.write(accOpenData['trans_type'] + ", " + accOpenData['trans_time'] + ", " + accOpenData['prev_bal'] + ", " + accOpenData['trans_amount'] + ", " + accOpenData['balance'] + '\n')
        accFile.close()
        option = showMenuOptions()
        if option == 'd':
            depositAmount(fileName)
        elif option == 't':
            displayTransactions(fileName)
        elif option == 'w':
            withdrawAmount(fileName)
        else:
            print("Closing account and all transactions")
    else:
        option = showMenuOptions()
        if option == 'd':
            depositAmount(fileName)
        elif option == 't':
            displayTransactions(fileName)
        elif option == 'w':
            withdrawAmount(fileName)
        else:
            print("Closing account and all transactions")


initiateApp()