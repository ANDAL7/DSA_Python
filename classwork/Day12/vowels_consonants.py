word=input()
vow=0
sp=0
for i in word:
    if i == 'a' or i=='e' or i=='i' or i=='o' or i=='u':
        vow+=1
    if i == " ":
        sp +=1
print("Vowels:",vow)
print("Consonants:",len(word)-vow-sp)