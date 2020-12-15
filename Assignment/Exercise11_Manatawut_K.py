inputHeight = int(input("The Height of the Pyramid : "))
for i in range(inputHeight):
    print(" "*(inputHeight-i-1),"*"*(2*i+1))
