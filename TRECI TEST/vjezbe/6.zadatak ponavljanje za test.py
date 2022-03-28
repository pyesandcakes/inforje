#Upišite string S koji je gramatička rečenica bez gramatičkih znakova. Izbacite najdulju riječ iz stringa S.
s=input('unesi recenicu bez gramatickih znakova')
ind=s.split()
r={}
r2d2={}
keylist=[]
p= ''
for i in ind:
    key=len(i)
    keylist.append(key)
    if(key in r):
        l=[]
        l.append(i)
        l.append(r[key])
        r.update({key:i})
    else:
        r.update({key:i})
keylist.sort(reverse=True)
for i in keylist:
    r2d2.update({i:r.get(i,0)})
for i in keylist:
    p+=r2d2[i]
    p+= ' '
print(p)