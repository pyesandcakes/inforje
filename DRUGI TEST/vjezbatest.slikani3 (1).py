#Upiši n prirodnih brojeva i spremi ih u listu l. Promjenite poredak elemenata u listi l tako da ih sortirate po njihovoj prosjećnoj vrijednosti znamenki.
n=int(input("Koliko znamenka želiš?"))
l=[]
for i in range(n):
    l.append(int(input("Upiši broj:")))
prosjek=0
privremeno=[]
for i in l:
    a=[]
    b=0
    c=0
    while(i>0):
        a.append(i%10)
        i=i//10
    for j in a:
        prosjek+=j
    b+=len(a)
    c=prosjek/b
    privremeno.append(c)
rj=[]
for i in range(n):
    t=privremeno.index(min(privremeno))
    rj.append(l.pop(t))
    privremeno.pop(t)
print(rj)
