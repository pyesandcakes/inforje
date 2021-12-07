#unesi prirodan broj i ispisi njegov broj znnemnki, zbroj znamenki i umnozak znamenki
n=int(input('unesi broj n'))
provjera=n
znamenka=0
brojac=0
zbrojzanmenki=0
umnozakzanmenki=1
while(n>0 and n!=0):#postavljamo uvijet za vadenje znamenaka, ako je n 0 onda idem
    znamenka=n%10#vadimo znamenku
    n=n//10
    brojac+=1#brojimo znamenke
    zbrojzanmenki+=znamenka#zbrajamo znamenke
    umnozakzanmenki*=znamenka#mnozimo znamenke
if(provjera==0):#ako nam je orginalni broj 0 onda samo ispisuje 0
    print('broj znamenki',0)
    print('zbroj znamenki:;',0)
    print('umnozak znamenki:',0)
else:#u suprotnom ispisujemo sta smo izracunali
    print('broj znamenki',brojac)
    print('zbroj znamenki:;',zbrojzanmenki)
    print('umnozak znamenki:',umnozakzanmenki)
    
