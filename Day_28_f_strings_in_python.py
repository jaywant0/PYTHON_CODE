# String formatting in python
# This method is complicated 
letter = "hey my name is {} and I am from {}"
country = "india"
name = "jaywant"

print(letter.format(name,country))

#f string as follows
print(f"Hey my name is {name} and I am from {country}")

txt = "for only {price:.2f} dollars !"
print(txt.format(price = 49.09999))

print(f"Hey my name is {{name}} and I am from {{country}}")