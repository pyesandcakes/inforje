#Spremite u riječnik n prirodnih brojeva gdje im je ključ najmanja znamenka. Ako ima više s istom najmanjom znamenkom spremite ih kao listu
n=int(input('unesi broj clanova'))
r={}
for i in range (n):
    broj=int(input('unesi broj'))
    znamenka=0
    min=9
    k=broj
    while(k>0):
        znamenka=k%10
        k=k//10
        if(min>znamenka):
            min=znamenka
    if(r.has_key(min)):
        l=[]
        l.append(broj)
        l.append(r[min])
        r.update({min:broj})
    else:
        r.update({min:broj})
    print(r)
