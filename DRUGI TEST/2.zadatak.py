##Upiši prirodan broj n, te n prirodnih brojeva koje spremamo u listu l na način da osigurate da niti jedna dva susjedna broja nemaju iste znamenke jedinica. Ako to nije moguće printajte "Nemoguće ubacivanje broja " gdje je x koji nije moguće ubaciti. Nakon svakog ubacivanja printajte listu.
n=int(input('unesi broj brojeva'))
l=[]
l.append(int(input('Unesi broj:')))
for i in range(n-1):
    x=int(input('Unesi broj:'))
    j=x%10
    if(j!=l[0]%10):
        l.insert(0,x)
    else:
         for k in range(len(l)):
             if(l[k]%10!=j and (l[k+1]%10!=j)):
                l.insert((k+1),x)
                break
                print(l)
         if(k==len(l)-1): 
            if(l[k]%10!=j):
                l.append(x)
                print(l)
            else:
                print('nemoguce')
                break
print(l)
