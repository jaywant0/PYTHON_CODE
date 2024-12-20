l = [1,2,3,4,5,6]
print(l)
print("Add element at last")
l.append(7)  # simplye add element in last of list
print(l)

l.reverse()  # reverse the list
print("Reverse the list")
print(l)

j = [3,2,5,7,4,3,1,1,1,1,8,1] 
j.sort()  # sort the list
print("sort the list")
print(j)

j.sort(reverse=True)
print("reverse sort the list")
print(j)

print("counting the numbers")
print(j.count(1))

k = [1,3,4,5,6]
# m = k
# m[2] = 0
# print(k)

print("copying the list")
n = k.copy()
print(n)

k.insert(1,499) # insert 499 at index 1 in k list
print("insert 499 at index 1 in k list")
print(k) 


g =[890,432,1342,342,230]
h =[243,1,3,43,343]

w = g + h  # merge the list in w
print(w)



