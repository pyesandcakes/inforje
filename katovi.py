#bandic gradi sarene nebodere a b i c katove, nakon sto su izgradeni je imao super ideju da
#bi bilo kul da svi neboderi imaju jednake katove. Koliko najmanje katove se treba izgraditi da tri nebodera imaju jednake katove
a=int(input("Koliko katova ima"))
b=int(input("Koliko katova ima"))
c=int(input("Koliko katova ima"))
prosjek=((a+b+c)//3)
if (a>prosjek or a<prosjek or a==prosjek):
    if a>prosjek:
        aa=a-prosjek
    if a<prosjek:
        aa=a-prosjek
    if a==prosjek:
        aa=0
if (b>prosjek or b<prosjek or b==prosjek):
    if b>prosjek:
        bb=b-prosjek
    if b<prosjek:
        bb=b-prosjek
    if b==prosjek:
        bb=0
if (c>prosjek or c<prosjek or c==prosjek):
    if c>prosjek:
        cc=c-prosjek
    if c<prosjek:
        cc=c-prosjek
    if c==prosjek:
        cc=0
if aa>prosjek:
    print("Prva zgrada treba srusiti", aa, "katova")
if aa==0:
    print("Prva zgrada ne treba vise katova")
if aa<prosjek:
    if aa<0:
        aa*=-1
    print("Prva zgrada treba jos", aa, "katova")
    

if bb>prosjek:
    print("Druga zgrada treba srusiti", bb, "katova")
if bb==0:
    print("Druga zgrada ne treba vise katova")
if bb<prosjek:
    if bb<0:
        bb*=-1
    print("Druga zgrada treba jos", bb, "katova")
    

if cc>prosjek:
    print("Treca zgrada treba srusiti", cc, "katova")
if cc==0:
    print("Treca zgrada ne treba vise katova")
if cc<prosjek:
    if cc<0:
        cc*=-1
    print("Treca zgrada treba jos", cc, "katova")
#print(prosjek)
#print(aa,bb,cc)
