
#2.tuple
t=0,9,8,"cat","car"
print(type(t))
t=(7,4,8,2,"ccc",7)
print(type(t))
print(t[0])
#t[0]=98# tuple va;ues cannot be changd or reassigned
print(t)
print(t.count(7))# lik list it see who many same  value as argument is present
print(t.index(8))# it tll the value is prsent on what indx on tuple.
print(t*2)
tu=(8,6,"car")
print(t+tu)
for i in t:
    print(i)
# it only has two dot operation
