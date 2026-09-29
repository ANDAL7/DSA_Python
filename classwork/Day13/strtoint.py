word = input()
word_lis = word.split()
for i in range(len(word_lis)):
    if word_lis[i].isdigit():
        continue
    else:
        a = int(word_lis[i-1])
        b = int(word_lis[i+1])
        if word_lis[i]=="+":
            print(a+b)
        elif word_lis[i]=="-":
            print(a-b)
        elif word_lis[i]=="*":
            print(a*b)
        else:
            c = round(a/b)
            print(c,a-(c*b))