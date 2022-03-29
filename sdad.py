s=input("")
br=0
br2=0
w=s.split()
for item in w:
   br+=1
for i in range(br):
    index = w.index(w[i])
print(index)