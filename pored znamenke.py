n=int(input())
tn=0
br=0
while(n>0):
    zn=n%10
    dn=(n//10)%10
    if(zn==dn or zn==tn):
        br+=1
    n=n//10
    tn=zn
print(br)