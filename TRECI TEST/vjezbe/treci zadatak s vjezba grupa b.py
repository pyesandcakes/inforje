#Koristeći riječnik sortirajte n prirodnih brojeva po njihovoj znamenci jedinica.
n=int(input('Upisi'))
r={}
for i in range(n):
    x=int(input(''))
    k=x
    jedinica=k%10
    r.update({x:jedinica})
sort=sorted(r.items(), key = lambda kv:(kv[1], kv[0])) #ovo iskreno ne znam objasnit ali radi program
print(sort)