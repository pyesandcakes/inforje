#Upišite n prirodnih brojeva i spremite ih u riječnik sa ključem jednakim njihovoj prvoj znamenci. 
# Ispišite sve brojeve kojima je prva znamenka jednaka 3.
n=int(input('unesi broj brojeva'))
r={}
b=[]
for i in range(n):
    broj=int(input('unesi broj'))
    k=broj
    revs_number=0
    while(k>0):
        ostatak=k%10  
        k=k//10  
        if(0<k>10):
            z=k
    for i in range(1):
        z=revs_number%10
        if(z==3):
            b.append(broj)
    if(z in r):
        l=[]
        l.append(broj)
        l.append(r[z])
        r.update({z:l})
    else:
        r.update({z:broj})
    print(r)
print(b)