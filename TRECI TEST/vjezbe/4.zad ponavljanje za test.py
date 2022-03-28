#Upišite string S koji je gramatička rečenica bez gramatičkih znakova. Izbacite najdulju riječ iz stringa S.
s=input('unesi recenicu bez gramatickih znakova ')
longest = max(s.split(), key=len)
s=s.replace(longest, '')
print(s)