#Upiši n prirodnih brojeva. Svaki broj spremi u listu na mjesto x gdje je x jednak broju ponavljanja tog broja u listi prije dodavanja. Nakon svakog upisa ispišite listu.
n=int(input("Upiši broj:"))
l=[]
for i in range(n):
    a=int(input("Upiši znamenku:"))
    l.insert(l.count(a),a)
    print(l)

