#upisujes PRIRODAN broj n sve dok ne upises 0. treba ispisati zbroj i prosjek svih brojeva. ispisati prosjek pozitivnih i umnozak negativnih
#prirodni brojevi nisu negativni pa se to ondas ne radi niti se ne ubrajaju i ukupan zbroj i broj brojeva zato jher nisu prirodni
brojac=0
zbrojbrojeva=0
zbrojparnih=0
umnozakneparnih=0
brojacparnih=0
while True:
    n=int(input('unesi broj n'))#unosenje broja n
    if(n==0):#provjera jeli 0
        break
    if(n>0):#ako nije nula i prirodan je onda se brojac povecava i broj se nadodaje na postojece
        brojac+=1
        zbrojbrojeva+=n
print('broj prirodnih brojeva',brojac,'zbroj prirodnih brojeva',zbrojbrojeva,'prosjek prirodnih brojeva',(zbrojbrojeva/brojac))
