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
        revs_number = (revs_number * 10) + ostatak  
        k = k // 10  
        prvaznamenka=0
    for i in range(1):
        prvaznamenka=revs_number%10
        if(prvaznamenka==3):
            b.append(broj)
    if(prvaznamenka in r):
        l=[]
        l.append(broj)
        l.append(r[prvaznamenka])
        r.update({prvaznamenka:l})
    else:
        r.update({prvaznamenka:broj})
    print(r)
print(b)