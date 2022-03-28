#Upišite string s gdje je s gramatička rečenica. Promjenite poredak riječi tako da su sortirane po tome koliko slova 'a' sadrže.
s=input('unesi broj')
s=s.split(' ')
b=0
r={}
c=''
sortiranalista=[]
listakljuceva=[]
for i in s:
    b=i.count('a') or i.count('A')
    listakljuceva.append(b)
    if b in r:
        l=[]
        l.append(i)
        l.append(r[b])
        r.update({b:l})
    else:
        r.update({b:i})
listakljuceva.sort(reverse=True)
for i in listakljuceva:
   sortiranalista.append(r[i])
print(sortiranalista)