#Upiši n prirodnih brojeva i spremi ih u listu. Izbaci iz liste broj koji ima najmanje istih znamenaka. Ispišite listu nakon izbacivanja i ponavljajte ovaj postupak dok ne izbacite sve brojeve.
n=int(input("Koliko znamenaka želiš?"))
l=[]
for i in range(n):
    l.append(int(input("Upiši broj:")))
p=[]
for i in l:
    a=i
    lol=[]
    br=0
    while(a>0):
        lol.append(a%10)
        a=a//10
    for i in lol:
        for j in lol:
            if(i==j):
                br+=1
    p.append(br)
for i in range(n):
    print(l)
    t=p.index(min(p))
    l.pop(t)
    p.pop(t)
print(l)
