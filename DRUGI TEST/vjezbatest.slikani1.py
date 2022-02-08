#Upiši prirodan broj n, te n prirodnih brojeva koje spremamo u listu l. Napravi sljedeće radnje u ovom poretku (nakon svake radnje isprintajte listu:
#1.Izbaci najveći element
#2.Sortiraj listu
#3.Dodaj najmani element liste na prvo mjesto
#4.Dodaj listi[1,7,8] elemente liste l na kraj
#5.Printaj na kojem mjestu se nalazi najveći broj
#6.Printaj koliko ima sedmica u listi te koliko lista ima elemenata.
n=int(input("Upiši koliko članova želiš:"))
l=[]
for i in range(n):
    l.append(int(input("Upiši član:")))
print(l)
l.remove(max(l))
print(l)
l.sort()
print(l)
#već je najmanji na početku jer smo sortali? Do i do anything?
print(l)
t=[1,7,8]
l+=t
print(l)
print(l.index(max(l)))
brsedmica=0
for i in l:
    if(i==7):
        brsedmica+=1
print(brsedmica)
print(len(l))
