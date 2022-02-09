n=int(input())
l=[]
l.append(int(input()))
a=int(input())
c=0
if(a%10!=l[0]%10):
    l.append(a)
else:
    print('nemoguće')
    c+=1
for i in range(n-2):
    a=int(input())
    zn=a%10
    nijeubaceno=True
    if(l[0]%10!=zn):
        l.insert(0,a)
        nijeubaceno=False
    else:
        for j in range(len(l)-1):
            if(l[j]%10!=zn and l[j+1]%10!=zn and nijeubaceno==True):
                l.insert(j+1,a)
                nijeubaceno=False
    if(nijeubaceno==True and zn!=l[len(l)-c]%10):
        l.append(a)
        nijeubaceno=False
    if(nijeubaceno==True):
        print('nemoguće')
    print(l)
    
