# sets
# sets are that data structure which in values are arranged authomatically to different index , sets does not allow same value to occur,w can add or remove data after its cretion
s={9,"happy","apple",99,9,"how are you"}# ifd you same value it automatically remove one from sets
print(s)
l=[8,9,9,"hello",77,65,"happy"]
print(type(l))# list
y=set(l)# convert list into set
print(type(y))
print(y)
t=(9,67,64,"car","coffee")
print(type(t))# tuple
u=set(t)# convert tuple in to set
print(type(u))
print(u)
s={6,8,9,3,"coffee","tea"}
print(s)
t=(0,9,8,8)
print(t)
t=("how",9,5,5,"coffee")
print(t)
print(s)
#s[0]=99 # you can not reassign 
#print(s[0])# you cannot access each index in set 
print(s.add("45"))# it used to add in set location is not permanent it can be changd autoatically
print(s)
#print(s[0:5])
y={95,115,"no",45,"carrr","happyÿ","apple",999}
print(s.update(y))# it is used to add elements of y in s
print(s)
print(y)
print(s.difference(y))# it show only value of s which is not present in y
y.add(996)
print(y.difference(s))# it only show values of y which is not present in s
fruit={"apple","mango","cherry","pineapple","pinecherry","pinemango","45"}
print(fruit.remove("cherry"))# it is usd to remove element from sets
print(fruit)
print(fruit.discard("apple"))# it works same as remove but it has one difference
print(fruit)
print(fruit.discard("orange"))# which is if element not present it cannot error 

print(fruit.pop())# no argument is needed it authomatically remove first element if you give it caus error
print(fruit)
fruit.union(s)# it add all elemenyty of s in fruit if occur same not add two time appear one time
print(fruit)
print(fruit.intersection(s))# it only show same element
