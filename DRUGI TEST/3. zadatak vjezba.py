#Upiši n prirodnih brojeva. Spremajte brojeve u listu na način da osigurate da broj nikad nema dva manja broja ispred sebe. Nakon svakog upisa ispišite listu.
n=int(input("Upiši broj znamenaka:"))
l=[]
for i in range(n):
    l.append(int(input("Upiši broj:")))
l.sort()
l.reverse()
print(l)
