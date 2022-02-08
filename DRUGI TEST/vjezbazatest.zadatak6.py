#Upiši n prirodnih brojeva i spremi ih u listu. Promjeni poredak elemenata u listi tako da ih sortirate po udaljenosti od prosjeka svih brojeva.
n=int(input("Koliko brojeva u listi želiš?"))
l=[]
r=[]
pro=0
for i in range(n):
    l.append(int(input("Upiši znamenku:")))
for i in l:
    pro+=i
pro=pro/len(l)
for i in l:
    r.append(abs(i-pro))
rj=[]
for i in range(n):
    t=r.index(min(r))
    rj.append(l.pop(t))
    r.pop(t)
print(rj)
