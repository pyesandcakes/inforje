#Upiši n prirodnih brojeva i spremi ih u listu l. Promjenite poredak elemenata u listi l tako da ih sortirate po njihovoj prosjećnoj vrijednosti znamenki.
n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
p=[]
for i in l:
    prosijek=0
    br=0
    while(i>0):
        zn=i%10
        i=i//10
        prosijek+=zn
        br+=1
    prosijek=prosijek/br
    p.append(prosijek)
r=[]
for i in range(len(l)):
    t=p.index(min(p))
    r.append(l.pop(t))
    p.pop(t)
print(r)
    
        
