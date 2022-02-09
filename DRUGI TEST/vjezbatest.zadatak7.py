#Upiši n prirodnih brojeva i spremi ih u listu. Promjeni poredak elemenata u listi tako da ih sortirate po broju znamenaka djeljivih s 3.
n=int(input("Koliko znamenka želiš?"))
l=[]
p=[]
br=0
for i in range(n):
    l.append(int(input("Upiši broj:")))
for i in l:
    br=0
    while(i>0):
        a=i%10
        if(a%3==0):
            br+=1
        i=i//10
    p.append(br)
rj=[]
for i in range(n):
    t=p.index(min(p))
    rj.append(l.pop(t))
    p.pop(t)
rj.reverse()
print(rj)
