#napisi broj u bazi 3 i ispisi koliko ima razlicitih znamenki.
#ovako ga je on napisao ali iz nekog zarloga ne radi za 0
n=int(input('unesi broj n u bazi tri'))
nula=0
jedan=1
dva=2
znamenka=0
while(n>0):
    znamenka=n%10
    n=n//10
    if(znamenka==nula):
        nula=1
    if(znamenka==jedan):
        jedan=1
    if(znamenka==dva):
        dva=1
print('broj 1',jedan)
print('broj 2',dva)
print('broj 0',nula)
