n=int(input(""))
br=0
prviniz=""
druginiz=""

while(n>0):
   zn=n%10 
   n=n//10
   if (br%2==0):
      prviniz=str(zn)+prviniz
   else:
      druginiz=str(zn)+druginiz
   br+=1
 if(br%2==0):
   print(prviniz)
else:
   print(druginiz)
 
