# manipulating tuples

countryies = ("spain","italy","india","England","Germany")

temp = list(countryies)
temp.append("russia")  # add item
temp.pop(3)            # remove item
temp[2] = "Finland"    # change item
countryies = tuple(temp)
print(countryies)

# tuples are not converting directly

tuple1 = (1,2,3,4,3,3,5,3,2,3,5,9,9,8,8,7,7,6,6,8,9)
res = tuple1.count(3)
print("count of 3 in tuple 1 is :",res)
res2 = tuple1.index(3)
print("the occuranace of 3 is :",res2)

res3 = tuple1.index(3,4,6)
print(res3)