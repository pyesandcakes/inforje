#Upišite string S koji je gramatička rečenica bez gramatičkih znakova. Obrnite svaku riječ.
s=input('unesi recenicu bez recenicnih znakova')
s=s.split(' ')
p=''
for i in s:
    rev=''.join(reversed(i))
    p+=rev
    p+=' '
print(p)
