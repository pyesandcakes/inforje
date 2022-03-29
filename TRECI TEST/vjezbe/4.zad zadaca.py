#Upisujemo kompresiranu poruku. Kompresirana poruka je oblika NS gdje je N broj ponavljanja broja S. 
#Dakle, poruka 2A3b je zapravo poruka AAbbb. 
#Napišite program koji dekompresira poruku i ispisuje ju.
n=input()
a=int(n[0])
b=int(n[-2])
print(a *n[1],b *n[-1])