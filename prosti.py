br=0
brpr=0
a=int(input())
for i in range (2,a+1):
    if a%i!=0:
        br+=1
    if br<2:
        brpr+=1
print(brpr)