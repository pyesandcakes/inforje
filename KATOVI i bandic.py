#bandic gradi sarene nebodere a b i c katove, nakon sto su izgradeni je imao super ideju da
#bi bilo kul da svi neboderi imaju jednake katove. Koliko najmanje katove se treba izgraditi da tri nebodera imaju jednake katove
a=int(input("Koliko katova ima"))
b=int(input("Koliko katova ima"))
c=int(input("Koliko katova ima"))
t=a+b+c-max(a,b,c)-min(a,b,c)
min=max(a,b,c)-t
max=min+t
print (max,t,min)
