#Ruska obaviještajna služba vas moli da za njih obavite jedan poslić. 
#Oni će upisati listu od n zabranjenih riječi koje vi morate cenzurirati iz upisanog stringa. 
#Cenzurirate riječ tako da joj zamjenite svaki simbol s "#"

n=int(input('Koliko rijeci za red list'))
for i in range (n):
    l=[]
    l.append(input('Cenzurirane rijeci'))
    print(l)
s=input('Rijeci')
words=s.split()
for i in range(len(words)):             
        if words[i] in l:                       
            words[i] = "#"*len(words[i])
print(' '.join(words))