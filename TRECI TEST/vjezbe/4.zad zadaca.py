#Upisujemo kompresiranu poruku. Kompresirana poruka je oblika NS gdje je N broj ponavljanja broja S. 
#Dakle, poruka 2A3b je zapravo poruka AAbbb. 
#Napišite program koji dekompresira poruku i ispisuje ju.
n=input()
r=''
for i in range(len(n)):
    if n[i].isdigit():
        r=r+int(n[i])*n[i+1]
print(r)
