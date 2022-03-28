#Upišite n prirodnih brojeva i spremite ih u riječnik 
#(ako više brojeva ima isti ključ spremite ih kao listu) sa ključem jednakim 
#broju njihovih parnih znamenaka. Koliko brojeva ima 3 parne znamenke?

n=int(input())
r={}
for i in range(n):
    x=int(input())
    y=x
    br=0
    while(y>0):
        znam=y%10
        y//=10
        if znam%2==0:
            br+=1
    if br in r:
        l=[]
        l.append(r[br])
        l.append(x)
        r.update({br:l})
    else:
        r.update({br:x})
print(r[3])