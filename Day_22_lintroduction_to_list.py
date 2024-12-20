
l = [3,4,52,3,2,1,3,4,3,2]
print(l)
print(type(l))
print(l[0])
print(l[1])
print(l[2])

v = ["ram","sham","ghanshyam","sahoo"]
print(v)

s = [23,"ram","mann","maher",32,32,42,3,2]
print(s)
print(type(s))
print([len(l)-3])

if "jay" in s:
    print("yes")
else:
    print("no")



# list slicing
j = ["rahus", "vinay", "dev","don","munna bhaiya","rajesh","ramu","pamu","shubham"]
print(j)
print(j[1:])
print(j[1:-1])
print(j[0:8])
print("slicing from 1:9:3")
print(j[1:9:2])


# list comprehension
lst = [i for i in range(3)]
print(lst)

lst1 = [i for i in range(10) if i%2 == 0]
print(lst1)





