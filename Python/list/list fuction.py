 ## Practice data structures
#1.list
l=[7,"car",9,10 ,"office","tea",99]
a=l[0:4]# print from 0 which is start and end 1 less the stop index is given

print(a)
print(l[:])
print(l[:5])
 ##operation with list
y=98
la=[8,"ff",y,9]
##repetition
print(l*2)
###concatenation
### + multiple list
k=[9,54,"khh",95]
print(l+la+k)
###iteration mean for loop
for i in l:
    print(i)

### dot operation
print(l[1])
l[1]="peach"# used to change specific index value
print(l[1])
l.insert(2,98)#.insert() is used to add value at specific index but donot change the value that is present at that position it move the old of the index value to the next
print(l)

l.append("hello")# it add value to the end where the list value is end
print(l)

l.pop(1)# pop() is used to remove value from the list you give index as argument if not it automatically tremove last value
print(l)

l.extend("hh")# extend() you can give in the form of list argument or string depend you if string is more than 1 letter it assigned each variable at the new position in the end nd it can not take int without list as argument if you need to enter int you need to make list

print(l)
l.extend([6,"kh",99])
print(l)
print(l.count(99))# it used to tell the value that you give as argument how many time is present in the list like 99 apear 2 time.

print(l.index("office"))# count() func tell the value you enter as argument is present on what index.

l.remove(99)# remove is like pop it remove value but if you not give value not index in pop you need to give pop() argument as index  it give error
print(l)

l.reverse()# reverse is used to change the index or location of values you give in list 0 index value gos to end mean reverse it

print(l)
print(l[-1])
l=[4,6,2,8,3,99,11,45,66]
l.sort() # usedto sort valus as assencending order
print(l)
l.sort(reverse=True)# descending order5
print(l)

la=["c","aple","apple","mango"]
str(l)
la.sort(key=len) # usedto sort valus as assencending order
print(la)
len(l)
la.sort(key=len,reverse=True)# descending order5
print(la)

