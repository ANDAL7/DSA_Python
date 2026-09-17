word = list(map(int,input("Enter a word: ").split()))
k = int(input("Enter a character from the word: "))
for i in word:
    if i == k:
        word.remove(i)
        break
print(word)