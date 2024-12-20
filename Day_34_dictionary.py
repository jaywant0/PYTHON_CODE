
ep = {100:65,  101:78,  102:64, 103:40}
ep1 ={200 : 64 , 201:98, 202:100 , 203 : 40}

ep.update(ep1)
print(ep)
ep.clear()
print(ep)
ep1.pop(200)

# del ep1
print(ep1)