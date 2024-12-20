a = int(input("Enter your age :  "))
print("your age is: ", a)

# conditional operators
#   > , < , >= , <= , ==, !=

print(a>18)   # True  # input = 25
print(a<=18)  # false
print(a==18)   # false
print(a!=18)   # True


# if else statement
if(a>18):
    print("you can drive")  # the space is known as indentation
else:
    print("you cannot drive")


print("\n")


# if else elif else statement
num = int(input("Enter the value of num: "))  # input = -1 
if(num < 0):
    print("Number is negative.")
elif(num == 0):
    print("Number is Zero.")
elif(num == 999):
    print("Number is special.")
else:
    print("Number is positive.")

    print("i am happy now")  # always print no conncetion between if else block

print("\n")
# Nested if statements

num1 = 18
if(num1 < 0):
    print("number is Negative")
elif(num1 > 0):
    if(num1 <= 10):
        print("Number is between 1-10")
    elif(num1 > 10 and num1 <= 20):
        print("number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")
