#Koristeći metodu replace zamijenite sva velika slova sa malima te printate rješenje.
s=input("")
dul=len(s)
for i in range(dul):
    if (s[i].isupper()):
        s=s.replace(s[i],s[i].lower())
print(s)