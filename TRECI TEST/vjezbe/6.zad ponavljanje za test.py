s=input('unesi recenicu bez gramatickih znakova ')
longest = max(s.split(), key=len)
s=s.replace(longest, '')
print(s)