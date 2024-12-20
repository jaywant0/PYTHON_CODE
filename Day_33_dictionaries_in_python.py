

dic = {
    "harry":"human being",
    "Spoon": "object",
      1    :  "rahul",
      2    :  "jay",
      3    :  "Ramu",


}

print(dic["harry"])

print(dic)

print(dic.get(1))

# print(dic[21])  #errror

print(dic.get(21))

# for all key access

print(dic.keys())


print("for accessing the key in dictionary")
for key in dic.keys():
    print(dic[key])

