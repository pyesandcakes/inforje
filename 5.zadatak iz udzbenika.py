#upisi broj n i ispisi najvecu i najmanju znamenku
n=int(input('unesi broj n'))
znamenka=0
min=9
max=0
while(n>0):
    znamenka=n%10#vadimo znamenke
    n=n//10
    if(znamenka>max):#trazimo najvecu
        max=znamenka
    if(znamenka<min):#trazimo najmanju
        min=znamenka
print('najmanja znamenka je:',min)
print('najveca znamenka je :',max)
