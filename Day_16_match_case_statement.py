x  = int(input("Enter the value of x : "))

# x is the variable to match

match x:
    # if x is 0
    case 0:
        print("X is zero")
    # case with if-condition
    case 4:
        print("case is 4")
    case _ if x != 90:
        print(x,"is not 90")
    case _ if x != 80:
        print(x,"x is not 80")
    
    case _:
        print(x)

print("\n")

x = input("Enter your x ")

match(x):
    case 1:
        print("jay")
    case 2:
        print("om")
    case 3:
        print("ram")
    case _ if(x != 10):
        print("omkar is my name")
    
    case _:
        print("my name is jay")











