n=int(input(""))
zn=0
m=n
br=0
while(n>0):
    n=n//10
    br+=1
if(br%2!=0):
    zn=0    
    r=br//2+1
    for i in range (r):
        zn=m%10
        m=m//10
    print(zn)
else:
    zn=0
    p=br//2
    for i in range(p):
        zn=m%100
        m=m//10
    print(zn)
