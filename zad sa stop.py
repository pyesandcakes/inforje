n=0
p=0
zp=0
n=0
zn=0
while(n!="STOP"):
    n=input()
    if(n=="STOP"):
        break
    else:   
        n=int(n)
        if(n%2==0):
            p+=1
            zp=n
        else:
            n+=1
            zn=n
print("Parni", zp/p)
print("Neparni", zn/n)