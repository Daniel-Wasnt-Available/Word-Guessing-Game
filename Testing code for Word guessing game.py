word = ["cow","pig","cat"]
blanks = "_"*len(word)

print(word)
print(blanks)

guess = input("hi: ")

for letter in word:
    print(letter)
    
#for i in range( len(word)):
#    print(i,word[i], blanks[i])
userinput = ("type: ")
    
for n, i in enumerate(word):
    if i == (userinput):
        word[n] = (userinput)
        print(word)