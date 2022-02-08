#Upiši prirodan broj n, te n prirodnih brojeva koje spremamo u listu l na način da osigurate da niti jedna dva susjedna broja nemaju iste znamenke jedinica. Ako to nije moguće printajte "Nemoguće ubacivanje broja " gdje je x koji nije moguće ubaciti. Nakon svakog ubacivanja printajte listu.
n=int(input("Koliko znamenaka želite?"))
l=[]
l.append(int(input("Upiši znamenku:")))
a=0
for i in range(n-1):
    a=int(input("Upiši znamenku:"))
    b=0
    for i in range(len(l)):
        if(len(l)==1):
            if(a==l(0)):
               print("Nemoguće ubacivanje broja.")
            else:
               l.append(a)
            break
        if(l(b)!=a and l(b+1)!=a):
            l.insert(b,a)
            print(l)
            break
        b+=1
        if(b>len(l)):
            print("Nemoguće ubacivanje broja.")
            break
    
