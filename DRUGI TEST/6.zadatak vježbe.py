#Upiši n prirodnih brojeva i spremi ih u listu. Promjeni poredak elemenata u listi tako da ih sortirate po udaljenosti od prosjeka svih brojeva.

n=int(input('upiši broj'))
zbroj=0
prosjek=0
l=[]
p=[]
r=[]
for i in range(n):
    l.append(int(input('upiši broj')))
for el in l:
    zbroj+=el
prosjek=zbroj/n
print(prosjek)
for i in l:
    p.append(abs(i-prosjek))
    print(p)
for i in range(n):
    t=p.index(max(p))
    r.append(l.pop(t))
    p.pop(t)
    print(r)

        
    
    
        
    
        
        
             
