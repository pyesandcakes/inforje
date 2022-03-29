#Upišite n prirodnih brojeva u jednom redu odvojeni razmakom. 
#Spremite ih u listu i printajte sortiranu listu.
n=input("")
n=n.split()
l=[]
for i in n:
    l.append(int(i))
l.sort()
print(l)