n=int(input(""))
m=int(input(""))
if(n>m):
    n,m = m,n
for i in range(n,m):
    x=i
    brojnula=0
    while(i>0):
        ostatak=i%10
        if(ostatak==0):
            brojnula+=1
        i=i//10
        if (brojnula==1 and i==0):
            print(x)
            
