#Upiši n prirodnih brojeva i spremi ih u listu. Promjeni poredak elemenata u listi tako da ih sortirate po broju znamenaka djeljivih s 3.
n=int(input('upiši broj'))
l=[]
znamenka=0
b=[]
for i in range(n):
    l.append(int(input('broj')))
for i in l:
    brojac=0
    while(i>0):
        znamenka=i%10
        i=i//10
        if(znamenka%3==0):
            brojac+=1
    b.append(brojac)
print(b)
r=[]
for i in range(n):
    t=b.index(min(b))
    r.append(l.pop(t))
    b.pop(t)
    print(r)

    
