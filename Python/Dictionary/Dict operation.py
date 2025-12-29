# dictionary
h={"keys":"value","car":"toyota","marks":89}
print(type(h))
print(h)
print(h["car"])
print(h.get("marks"))# get is used to tell value of key that you give as argument in dic
print(h.get("hello"))# get also help if key is not persent it not error an assign it value none
print(h)
print(h.keys())# it show all keys only not value
h["carr"]="landcrusier"# add nw key
print(h)
h["car"]="Tooyota"# modify or rassign old car key
print(h)
print(h.values())# it show all the values only
print(h.items())# it makes tuple or group  of each key and his value in the list
h.update({"hello":90})# update is like reassign valu which is don up but in update in() you have folloe dictionary structure{"keys":"value"}
print(h)
print(h.setdefault("kon"))# if key present show it value otherwis if key notpresent it not error like get()function it give value none
print(h.pop("keys"))# in dictionar data structure pop need 1 argument as key other wise it erroer not like list if you not give it authomaticalyy rempove end value
print(h)
print(h.popitem())# it authomatically rmove end key no argument is needed
print(h)
d_copy=h
print(d_copy)
del(d_copy)
print(h)
print(h)
d=h.copy()# it make copy and store in variable but you can also do manually

print(d)
del (h)# it del the dic completely


d.clear()
print(d)# it only clear dic keys and values not del from memory
