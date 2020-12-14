usernameInput = input("Username : ")
passwordInput = input("Password : ")
product1 = 10900
product2 = 15900
userAmount1 = 0
userAmount2 = 0
if usernameInput == "manatawut":
    if passwordInput == "12345678":
        print("Login Success !!!")
        print("Welcome to NiNewqxzShop")
        print("Products in the Shop")
        print("1. CPU INTEL CORE I7 piece",product1,"Baht")
        print("2. CPU INTEL CORE I9 piece",product2,"Baht")
        userSelect1 = input("Do you want a CPU INTEL CORE I7 ?(Y/N) : ")
        if userSelect1 == "Y":
            userAmount1 = int(input("How many do you want ? : "))
        userSelect2 = input("Do you want a CPU INTEL CORE I9 ?(Y/N) : ")
        if userSelect2 == "Y":
            userAmount2 = int(input("How many do you want ? : "))
        print("-----Summary-----")
        if userAmount1 == 0 and userAmount2 == 0:
            print("Shopping Cart is Empty")
            print("Thank you for your visting")
        else:
            if userAmount1 != 0:
                print("CPU INTEL CORE I7 Quantity",userAmount1,"Piece",product1*userAmount1,"Baht")
            if userAmount2 != 0:
                print("CPU INTEL CORE I9 Quantity",userAmount2,"Piece",product2*userAmount2,"Baht")
            print("Total Piece",product1*userAmount1+product2*userAmount2)
            print("Thank you for your visting")
    else:
        print("Password Incorrect")
else:
    print("User Invalid")