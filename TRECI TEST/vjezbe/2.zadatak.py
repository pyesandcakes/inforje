#Upišite gramatičku rečenicu te spremite sve njene riječi u listu. Hint: treba izbaciti sve rečenične znakove.
import string
l=[]
r=input('unesi string')
for character in string.punctuation:
    r=r.replace(character,'')
l.append(r)
print(l)
