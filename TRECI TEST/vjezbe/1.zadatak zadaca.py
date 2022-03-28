#Upišite string s gdje je s gramatička rečenica. Promjenite poredak riječi tako da su sortirane po tome koliko slova 'a' sadrže.
s=input('unesi broj')
s=s.split(' ')
br=0
r={}
sortiranalista=[]
listakljuceva=[]
l=[]
for i in s:
   b=i.count('a')
   print(b)
   listakljuceva.append(b)
   if(b in r):
       l.append(i)
       l.append(r[b])
       r.update({b:l})
