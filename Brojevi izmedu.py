#upisi dva prirodna broja i ispisi sve brojeve iz intervala a i b
a=int(input("Upisi prvi broj"))
b=int(input("Upisi drugi broj"))
if(a>b):
    max=a
    min=b
else:
    max=b
    min=a
c=min
for i in range(min,(max-1)):
    c+=1
    print(c)
