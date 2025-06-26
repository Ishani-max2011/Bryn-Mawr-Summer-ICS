
def Weight(fruits):
    weight = 4*fruits
    print(f"The weight of your fruits is {weight} pounds")

def Weight2(vegetables):
    weight = 3*vegetables
    print(f"The weight of your vegetables is {weight} pounds")

def printItems(items, prices):
    print("-----All Items----")
    for i in (items):
        print(f"Your grocery: {i}, price: ${prices[items.index(i)]}")

def totalBalance(cost, acct):
    print("-----Total Cost-----")
    cost = sum(cost)
    print(f"-----${cost}-----")
    final = acct - cost
    print(f"Here is your final balance: {final}")

def Debt(acct, cost):
    cost = sum(cost)
    if cost > acct:
        final = acct - cost
        print(f"You are in debt by {final} dollars")
    else:
        print("You are not in debt! Yay!")

def Remove(groceries, prices, item):
    position = groceries.index(item) 
    groceries.pop(position)
    prices.pop(position)
    

def main():
    groceries = []
    prices = []
    name = input("Enter your name: ").strip()
    check = True
    while check == True:
        print(f"Welcome to Whole Foods {name}!")
        print("Pick which group of foods you want to shop for first!")
        print("1. Dairy")
        print("2. Fruits")
        print("3. Vegetables")
        print("4. Protein")
        print("5. Wheat")
        print("6. Condiments")
        print("7.Spices and Herbs")
        print("8. Quit")
        option = input("Enter your choice from above: ")
        if option.isnumeric() == True:
            if int(option) == 1:
                item = input("Enter the type of dairy you want: ").strip()
                price = int((input("Enter how many of this type you want: ")))
                prices.append(12*price)
                groceries.append(item)
            elif int(option) == 2:
                item = input("Enter type of fruits you want: ").strip()
                price = int((input("Enter how many of this type you want: ")))
                prices.append(10*price)
                groceries.append(item)
                Weight(price)
            elif int(option) == 3:
                item = input("Enter type of vegetables you want: ").strip()
                price = int((input("Enter how many of this type you want: ")))
                prices.append(8*price)
                groceries.append(item)
                Weight2(price)
            elif int(option) == 4:
                item = input("Enter type of protein you want: ").strip()
                price = int((input("Enter how many of this type you want: ")))
                prices.append(15*price)
                groceries.append(item)
            elif int(option) == 5:
                item = input("Enter the type of wheat you want: ").strip()
                price = int((input("Enter how many of this type you want: ")))
                prices.append(5.25*price)
                groceries.append(item)
            elif int(option) == 6:
                item = input("Enter type of condiment you want: ")
                price = int((input("Enter how many of this type you want: ")))
                prices.append(0.75*price)
                groceries.append(item)
            elif int(option) == 7:
                item = input("Enter the type of spice that you want: ")
                price = int((input("Enter how many of this type you want: ")))
                prices.append(0.25*price)
                groceries.append(item)
            elif int(option) == 8:
                print("Time to check out your groceries!")
                balance = int(input("Enter your balance: "))
                printItems(groceries, prices)
                totalBalance(prices, balance)
                Debt(balance, prices)
                check2 = True
                while check2 == True:
                    option = input(("do you want to remove any items?(type the item you want to remove if so): "))
                    if option in groceries:
                        Remove(groceries, prices, item)
                        printItems(groceries, prices)
                        totalBalance(prices, balance)
                        Debt(balance, prices)
                    elif option == "quit":
                        check2 = False
                print("Thank you for shopping with us! Goodbye!")
                check = False  
            else:
                print("That is not a valid input") 
        else:
            print("Please write down the number of your choice base off the list above")
                                         
main()