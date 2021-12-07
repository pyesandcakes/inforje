#u azurnoj udolini zive populacije voltreona i pikacua. svaki mjesec svaki voltreon pojede jednog pikacua,a nakon svake godine broj voltreona se udvostruci, a broj pikacua udesetero struci. Upisi broj pikacau i broj voltreona i broj mjeseci. 
# Program ispisuje stanje populacije nakon toliko mjeseci.
pika=int(input("Koliko pikachua ima?"))
volt=int(input("Koliko voltreona ima?"))
mjesec=int(input("Koliko mjeseci?"))
godina=0
if pika<volt:
    pika=0
for i in range(mjesec):
    pika-=volt
if mjesec>12:
    godina=mjesec//12
    for i in range(godina):
        pika=pika*10
        volt=volt*2
    quit
if pika<0:
    print("Nema vise pikachua")
else:
    print("Ima", pika,"pikachua")    
print("Ima", volt,"voltreona")