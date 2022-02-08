#Upiši n prirodnih brojeva. Svaki broj spremi u listu na mjesto x gdje je x jednak broju brojeva manjih od upisanog broj koji su već u listi. Nakon svakog upisa ispišite listu.
n=int(input("Upiši koliko članova želiš:"))
l=[]
for i in range(n):
    a=int(input("Upiši broj:"))
    br=0
    for i in l:
        if(i<a):
            br+=1
    l.insert(br,a)
    print(l)
            
    
