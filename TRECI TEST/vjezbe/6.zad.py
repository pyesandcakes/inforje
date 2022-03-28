#Upišite string S koji je gramatička rečenica bez gramatičkih znakova. Preslozite rijeci po njihovim duljinama.
s=input('unesi recenicu bez gramatickih znakova')
l=s.split()
z=sorted(l, key=len)
print(' '.join(z))           