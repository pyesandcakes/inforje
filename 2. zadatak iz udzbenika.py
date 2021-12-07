#unesi prirodan broj n i napisi ga u suprotnmom redosljedu
n=int(input('unesi broj n'))
znamenka=0
obrnutredoslijed=0
while(n>0):
    znamenka=n%10#vadimo znamenku sa kraja broja
    n=n//10
    obrnutredoslijed=obrnutredoslijed*10+znamenka#mnozimo obrnut raspored broja sa 10 svaki put te mu dodajemo znamneku
    #to radimo zato da preokrenemo redoslijed
print('obrnut redoslijed broja je:',obrnutredoslijed)
