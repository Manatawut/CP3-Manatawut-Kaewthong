def vatCal(totalPrice):
    result = totalPrice+(totalPrice*7/100)
    return result
a = int(input("Input Total Price : "))
print(vatCal(a))