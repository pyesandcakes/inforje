##Upiši prirodan broj n, te n prirodnih brojeva koje spremamo u listu l na način da osigurate da niti jedna dva susjedna broja nemaju iste znamenke jedinica. Ako to nije moguće printajte "Nemoguće ubacivanje broja " gdje je x koji nije moguće ubaciti. Nakon svakog ubacivanja printajte listu.
n=int(input('unesi broj brojeva'))
l=[]
a=0
b=0
for i in range(1):
    c=int(input('unesi broj:'))
    l.append(c)
for i in range(n-1):
    c=int(input('unesi broj:'))
    b=c
    a=c%10
    u=l[-1]%10
    if(a==u):
        print('ne mozes upisati taj broj!!')
        print(l)
    else:
        l.append(b)
        print('OMGGG bravo znas upisati broj sa razlicitom znamenkom jedinicaaaa!!!')
        print(l)
       
