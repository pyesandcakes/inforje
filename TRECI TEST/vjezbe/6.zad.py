s=input('unesi recenicu bez gramatickih znakova')
ind=s.split()
ind2=sorted(ind, key=len)
print(' '.join(ind2))           