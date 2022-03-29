#upisujemo n prirodnih brojeva i spremi ih u rjecnik sa kljucem broja njihovih znamenaka
n=int(input(''))
r={}
br=0
for i in range(n):
    x=int(input(''))
    k=x
    while(k>0):
        k=k//10
        br+=1
    if(br in r):
        l=[]
        l.append(x)
        l.append(r[br])
        r.update({br:l})
    else:
        r.update({x:br})
print(r)
