


s1 = {1,2,5,6}
s2 = {3,6,7}

print(s1.union(s2))
print(s1,s2)

s1.update(s2)
print(s1)

cities1 = {"Tokyo","madrid","Berlin","Delhi"}
cities2 = {"Tokyo","Seoul","kabul","madrid"}

print(cities1.intersection(cities2))

# cities1.intersection_update(cities2)
# print(cities1)

# cities3 = cities1.symmetric_difference(cities2)
# print(cities3)

# cities4 = cities1.difference(cities2)
# print("Difference funtion of two set",cities4)

# isjoint() methods intersection is null
print(cities1.isdisjoint(cities2))

# issuperset
print(cities1.issuperset(cities2))

# remove()
cities1.remove("Tokyo")
print(cities1)

#discard
cities2.discard("Tokyo")
print(cities2)

# del 
# del cities2
# print(cities2)






