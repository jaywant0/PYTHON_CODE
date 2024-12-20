a = "jaywant"

#strings are immuatable  we can't change it

print(len(a))     #output = 7r
print(a)
print(a.upper())  #output = JAYWANT
print(a.lower())  #output = jaywant

#here string a = not change just make new strings

b = "!!jay!!!!!"
print(b.rstrip("!")) #output = !!jay only last

c = "!!!!jay!!!jay!!"
print(c.replace("jay","omkar")) #output = omkar 
#replace all occurence of jay with omkar

d = "!!!jay!! !!!!! jay"
print(d.split(" "))
# split the string into list

e = "introduction to js"
print(e.capitalize()) #output = Introducton to js
#simple first letter to uppercase and other lowercase

f = "welcome to the console!!!"
print(len(f))
print(f.center(50))
print(len(f.center(50)))


g =  "!! jay !!!jay@@@ jay#$#"
print(g.count("jay"))  #output = 3

h = "welcome to the console !!!"
print(h.endswith("!!!"))
# uses like boolean

i = "he's name is dan . he is an honest man."
print(i.find("is"))  #output = 10 first occurence of is
print(i.index("is"))  #output = 10

j = "WelvomeTotheconsoloe"
print(j.isalnum()) # A-Z or a-z or 0-9 no special charcter

k = "welcome"
print(k.isalpha())

L = "Welcome"
print(L.islower()) # output = false

M = " "
print("M = ",M.isspace())  # output = True


N =  "World health organization"
print("N = ", N.istitle())

O = "python is interpreted language"
print("O = ",O.startswith("python"))

P = "python is interpreted language"
print("p = ",P.swapcase())
#uppercase to lowercase and lowercase to uppercase

P = "PYTHON IS INTERPRETED LANGUAGE"
print("p = ",P.swapcase())
#uppercase to lowercase and lowercase to uppercase

Q =  "His name is Dan.Dan is an honest man "
print("Q = " ,Q.title())
#make first letter to capital



'''
1.  len()
2.  uppercase()
3.  lowercase()
4.  rstrip()
5.  replace()
6.  center()
7.  spilit()
8.  count()
9.  endswith()
10.  startwith()
11.  isalnum()
12.  isalpha()
13.  isspace()
14.  istitle()
15.  title()
16.  capitalize()
17.  swapcase()
18.  find()
19.  index()



'''
 



 
  