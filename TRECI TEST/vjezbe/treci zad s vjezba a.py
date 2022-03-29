#Upišite listu od n prirodnih brojeva i sortirajte ih po srednjoj vrijednosti njihovih znamenaka. 
#Obavezno koristite riječnike.
n=int(input(''))
l=[]
r={}
sort={}
for i in range(n):
    x=input("")
    l.append(int(x))
    dul=int(len(x))
    srednja=sum(l)/dul
    r.update({x:srednja})
sort=sorted(r.items(), key = lambda kv:(kv[1], kv[0]))
print(sort)