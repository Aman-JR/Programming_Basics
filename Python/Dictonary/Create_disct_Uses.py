# Creation of the dictonary and uses

d1 = {
    1 : "Chair",
    2 : "Table",
    3 : "Bag",
    4 : "Laptop"
}

print(d1)

# Accessing the element in Dictonary
print(d1.get(1))

# Accessing the keys of the dictonary

All_keys = d1.keys()
print(All_keys)

# Accessing onl Values

All_values = d1.values()
print(All_values)


# Accessing the key value pairs

for itm in d1:
    print("Item No."+str(itm)+" contains : "+d1[itm])

# CReating the Dictonary from scratch
d2 = {}
d2.update([("Aman",92),("Ashish",98)])
print(d2)
print(d2.keys())

# setting the Dictonary for the use of the work in the use of the Program

d3 = {}
d3.update([("What are the use of the work", 1), ("See the work first and then do teh following", 2)])
print(d3)


li = [1,1,1,1,2,1,1,1]
print(li)
li.remove(1)
print(li)
