#3. From given list:
#gadgets = ["Mobile", "Laptop", 100, "Camera", 310.28, "Speakers", 27.00,
#"Television", 1000, "Laptop Case", "Camera Lens"]
#a) Create separate list of strings and numbers
#b) Sort the string list in ascending order
#c) Sort the string list in descending order
#d) Sort the number list in ascending order
#e) Sort the number list in descending order


#a) Create separate list of strings and numbers
gadgets = ["Mobile", "Laptop", 100, "Camera", 310.28, "Speakers", 27.00,
"Television", 1000, "Laptop Case", "Camera Lens"]
lstring=[]
linteger=[]
for item in gadgets:
    if isinstance(item,str):
        lstring.append (item)
    elif isinstance(item,(int,float)):
        linteger.append (item)



print(lstring)
print(linteger)


#b) Sort the string list in ascending order

lstring.sort()
print(lstring)

#c) Sort the string list in descending order
lstring.sort(reverse=True)
print(lstring)


#d) Sort the number list in ascending order
linteger.sort()
print(linteger)



#e) Sort the number list in descending order
linteger.sort(reverse=True)
print(linteger)

