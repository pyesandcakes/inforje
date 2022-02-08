#Upiši n prirodnih brojeva i spremi ih u listu. Izbaci iz liste broj koji ima najmanje zajedničkih djelitelja sa preostalim brojevima u listi. Ispišite listu nakon izbacivanja i ponavljajte ovaj postupak dok ne izbacite sve brojeve.
n=int(input("Koliko znamenaka želiš?"))
l=[]
for i in range(n):
    l.append(int(input("Upiši znamenku:")))
privremeno=[]
for i in l:
    br=0
    for j in l:
        for k in range(1,min(i+1,j+1)):
            if(i%k==0 and j%k==0):
                br+=1
    privremeno.append(br)
print(l)
for i in range(n):
    t=privremeno.index(min(privremeno))
    l.pop(t)
    print(l)
    privremeno.pop(t)
