n=int(input("n broj"))
m=int(input(""))
if(n>m):
    n,m = m,n
for i in range (n,m):
    x=i
    while(i>0):
        zn=i%10
        i=i//10
        if (zn==1 and zn==2 or zn==1 or zn==2):
            print(x)
            break
