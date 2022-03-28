#Upišite n prirodnih brojeva i spremite ih u riječnik 
#(ako više brojeva ima isti ključ spremite ih kao listu) sa ključem jednakim “Prost” ako 
#je broj prost ili “Složen” ako je broj složen. 
#Ispišite one brojeve kojih ima više.

n=int(input())
r={}
for i in range(n):
    x=int(input())
    prost=True
    for i in range(2, x):
        if x%i==0:
            prost=False
    if prost:
        if 'Prost' in r:
            l=[]
            l.append(r['Prost'])
            l.append(x)
            r.update({'Prost':l})
        else:
            r.update({'Prost':x})
    else:
        if 'Slozen' in r:
            l=[]
            l.append(r['Slozen'])
            l.append(x)
            r.update({'Slozen':l})
        else:
            r.update({'Slozen':x})
print(r)