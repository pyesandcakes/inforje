#Rastavite upisani string na listu riječi, bez rečeničnih znakova (. , ! ? ...)
import string
l=[]
r=input('unesi string ')
for character in string.punctuation:
    r=r.replace(character,'')
l.append(r)
print(l)
