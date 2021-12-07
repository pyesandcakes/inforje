n=int(input('unesi broj n'))
novaznamenka=0
n2=n
znamenka=0
brojac=0
brojac2=0
max=0
while(n>0):
    znamenka=n%10
    n=n//10
    brojac+=1
    if(znamenka>max):
        max=znamenka
while True:
    novaznamenka=n2%10
    n2=n2//10
    brojac2+=1
    if(novaznamenka==max):
        break
print('pozicija najvece znamenke je:',((brojac-brojac2)+1))
