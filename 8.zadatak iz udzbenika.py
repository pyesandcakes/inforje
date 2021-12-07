#upisi prirodan broj n te najmanji broj ciji je kvadrat jednak ili veci broju n
n=int(input('unesi broj n'))
a=0
while(a*a<n):#provjeravamo kvadrate
    a+=1#povecavamo ga
print(a)
