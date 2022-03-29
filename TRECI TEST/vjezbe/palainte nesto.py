s=input("")
s=s.split(" ")
br=0
for i in s:
    o=i[::-1]
    if(i==o):
        br+=1
print(br)
