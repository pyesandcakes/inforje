n=int(input('unesi broj brojeva'))
l=[]
b=[1,7,8]
for i in range(n):
    b=int(input('unesi brojeve'))
    l.append(b)
l.remove(max(l))
print(l)
l.sort()
l.insert(1,min(l))
print(l)
c=l[:]
for j in l:
    b.append(j)
print(b)
b.index(max(b))
