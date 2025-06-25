
def createAccount(name, balance, accts):
    accts[name] = balance
    

def closeAccount(accts, name):
    if name in accts.keys():
        accts.pop(name)
    else:
        print("That is not a valid accout name")


def withdraw(name, amount, accts):
    if name in accts.keys():
        if amount > accts[name]:
            print("amount exceeds account balance")
            return False
        else:
            accts[name] = accts[name] - amount
            return True
    else:
        print("That is not a valid accout name")
        return False

def deposit(name, amount, accts):
    if name in accts.keys():
        accts[name] = accts[name] + amount
    else:
        print("That is not a valid accout name")

def transfer(acct1, acct2, amount, accts):
    if acct1 in accts.keys() and acct2 in accts.keys():
        if withdraw(acct1, amount, accts) == True:
            deposit(acct2, amount, accts)
    else:
        print("One of those accounts is not a valid accout name")

def main():
    accounts = {"John Pork": 500.0}
    check = True
    while check == True:
        print("Welcome to the bank")
        print("1. Create Account")
        print("2. Close Account")
        print("3. Withdraw")
        print("4. Deposit")
        print("5. Transfer")
        print("6. Quit")
        option = input("Enter your choice from above: ").strip()
        if option.isnumeric() == True:
            if int(option) == 1:
                acctname = input("Enter the name of your account: ").strip()
                balance = float(input("Enter your balance: "))
                createAccount(acctname, balance, accounts)
                print(accounts)
            elif int(option) == 2:
                acctname = input("Enter your name of account you wish to close: ").strip()
                closeAccount(acctname, accounts)
                print(accounts)
            elif int(option) == 3:
                acctname = input("Enter your name of account you wish to withdraw from: ").strip()
                amt = float(input("Enter amount you wish to withdraw: "))
                withdraw(acctname, amt, accounts)
                print(accounts)
            elif int(option) == 4:
                acctname = input("Enter your name of account you wish to deposit from: ").strip()
                amt = float(input("Enter amount you wish to deposit: "))
                print(accounts)
            elif int(option) == 5:
                acct1 = input("Enter the name of account you wish to transfer from: ").strip()
                acct2 = input("Enter the name of account you wish to transfer to: ").strip()
                amt = float(input("Enter amount you wish to transfer: "))
                transfer(acct1, acct2, amt, accounts)
                print(accounts)
            if int(option) == 6:
                print("Thanks for visiting!")
                check = False
        else:
            print("Invalid input")
main()
