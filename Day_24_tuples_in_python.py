
tup = (1,5,6)
print(type(tup),tup)
# tuples are not changes 
# tuples are same as list

print(tup[0])
print(tup[2])
print(len(tup))


if 4 in tup:
    print("yes present in tup")
else:
    print("no")

print("slicing of tuple ")
tup2 = tup[1:2]
print(tup2)