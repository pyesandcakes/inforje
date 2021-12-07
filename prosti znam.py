n=int(input())
zn=0
br=0
ukupno=0
while(n>0):
    zn=n%10
    n=n//10
    prost=1
    for i in range (2,zn):
        if(zn%i==0):
            prost=0
        else:
            prost+=1
ukupno+=prost
print("Ima", ukupno)