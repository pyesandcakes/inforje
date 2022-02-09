#Upiši n prirodnih brojeva i spremi ih u listu. Provodite sljedeću proceduru dok ne ispraznite cijelu listu: odredite broj x koji može najviše pute podjeliti brojeve iz liste (imajte na umu da x može više puta djeliti isti broj) te izbacite iz liste broj koji se najviše puta može podjeliti s x. Isprintajte listu nakon svakog izbacivanja.
n=int(input('unesi broj brojeva'))
x=int(input('Odredi broj x'))
l=[]
u=[]
for i in range(n):
    c=int(input('unesi broj:'))
    l.append(c)
for i in l:
    brojac=0
    a=i
    while(a>0):
        if(a%x==0):
            brojac+=1
            a=a//x
        else:
            break
    u.append(brojac)
print(l)
print(u)
for i in range(n):
    target=u.index(max(u))
    l.pop(target)
    u.pop(target)
    print(l)
    print(u)
