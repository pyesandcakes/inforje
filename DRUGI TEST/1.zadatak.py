#Upiši prirodan broj n, te n prirodnih brojeva koje spremamo u listu l. Napravi sljedeće radnje u ovom poretku (nakon svake radnje isprintajte listu:
#1.Izbaci najveći element
#2.Sortiraj listu
#3.Dodaj najmani element liste na prvo mjesto
#4.Dodaj listi[1,7,8] elemente liste l na kraj
#5.Printaj na kojem mjestu se nalazi najveći broj
#6.Printaj koliko ima sedmica u listi te koliko lista ima elemenata.
n=int(input('unesi broj brojeva'))
l=[]
b=[1,7,8]
for i in range(n):
    b=int(input('unesi brojeve'))
    l.append(b)
l.remove(max(l))
print(l)
l.sort()
l.insert(1,min(l))
print(l)
c=l[:]
for j in l:
    b.append(j)
print(b)
b.index(max(b))
