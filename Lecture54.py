def login():
    user = input("Username: ")
    pwd = input("Password: ")
    if user == "admin" and pwd == "111":
        showMenu()
    else:
        print("Wrong username or password")
        login()

def showMenu():
    print("---- Welcome to Shop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    menuSelect()

def menuSelect():
    userSelected = int(input("Please choose >>"))
    if userSelected == 1:
        print("Total Price included VAT =", vatCalculator(int(input("Please enter Total Price: "))))
        thankyou()
    elif userSelected == 2:
        priceCalculator()
    else:
        print("!!!Please select 1 or 2!!!")
        showMenu()

def vatCalculator(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result

def priceCalculator():
    price1 = int(input("First Product Price: "))
    price2 = int(input("Second Product Price: "))
    print("Total Price included VAT =", vatCalculator(price1 + price2))
    thankyou()

def thankyou():
    print("Thank you for shopping with us!")

login()