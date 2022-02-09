#Upiši n prirodnih brojeva i spremi ih u listu l. Promjenite poredak elemenata u listi l tako da ih sortirate po njihovoj prosjećnoj vrijednosti znamenki.
n=int(input('unesi broj brojeva'))
l=[]
u=[]
for i in range(n):
    c=int(input('unesi broj:'))
    l.append(c)
for i in l:
    b=0
    prosjek=0
    brojac=0
    while(i>0):
        brojac+=1
        b+=i%10
        i=i//10
    prosjek=b/brojac
    u.append(prosjek)
print(l)
print(u)
for i in range(n):
    target=u.index(min(u))
    l.append(l.pop(target))
    u.pop(target)
    print(l)
    print(u)
