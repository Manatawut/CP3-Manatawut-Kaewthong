inputHeight = int(input("The Height of the Pyramid : "))
for i in range(inputHeight):
    space = " "*(inputHeight-i-1)
    star = "*"*(2*i+1)
    print(space,star)
