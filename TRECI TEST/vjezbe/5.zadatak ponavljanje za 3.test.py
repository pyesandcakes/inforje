#Upišite string S koji je gramatička rečenica bez gramatičkih znakova. Obrnite svaku riječ.
s=input('unesi recenicu bez recenicnih znakova')
stringlength=len(s) # calculate length of the list
slicedString=s[stringlength::-1] # slicing 
print (slicedString) # print the reversed string