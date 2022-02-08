#Upiši n prirodnih brojeva i spremi ih u listu. Izbaci iz liste broj koji ima najveću znamenku. Ispišite listu nakon izbacivanja i ponavljajte ovaj postupak dok ne izbacite sve brojeve.
n=int(input("Koliko članova želiš?"))
l=[]
for i in range(n):
    l.append(int(input("Upiši brojček:")))
privremeno=[]
for i in l:
    a=0
    while(i>0):
        if(i%10>a):
            a=i%10
        i=i//10
    privremeno.append(a)
print(l)
for i in range(n):
    t=privremeno.index(max(privremeno))
    l.pop(t)
    print(l)
    privremeno.pop(t)
