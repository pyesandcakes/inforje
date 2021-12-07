n=int(input())
p=0
ne=0
zn=0
while(n>0):
    zn=n%10
    n//=10
    if(zn//2==0):
        p+=1
    else:
        ne+=1
    print(zn,"a")
    print(n,"b")

print("Ima",p ,"parnih i", ne , "neparnih")