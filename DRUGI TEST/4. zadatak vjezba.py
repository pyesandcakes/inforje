#Upiši n prirodnih brojeva. Spremajte brojeve u listu na način da osigurate da broj nikad nema zajedničkog djelitelja sa dva broja ispred sebe. Nakon svakog upisa ispišite listu.
n=int(input("Upiši broj znamenaka:"))
l=[]
a=0
for i in range(n):
    dje=0
    djel=0
    b=int(input("Upiši broj:"))
    if(len(l)<2):
        l.append(b)
    else:
        x=min(l[a],b)
        y=max(l[a],b)
        c=min(l[a+1],b)
        d=max(l[a+1],b)
        for i in range(3,x+1):
            if(x%i==0 and y%i==0):
                dje+=1
        if(dje>0):
            for i in range(3,c+1):
                if(c%i==0 and d%i==0):
                    djel+=1
        if(djel==1 and dje==1):
                l.insert(a+2,b)
        else:
            l.insert(a-1,b)
        a+=1
    print(l)
