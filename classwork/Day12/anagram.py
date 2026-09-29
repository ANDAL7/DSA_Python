"""word_1 = list(input())
word_2 = list(input())
if len(word_1)==len(word_2):
    for i in word_1:
        if i in word_2:
            word_2.remove(i)
        else:
            print("--")
            break
    if word_2 == []:
        print("yes")
else:
    print("--")
    """"""
fr
if len(word_1)==len(word_2):
    for i in word_1:
        fr_1[i] = fr_1.get(i,0)+1
    for i in word_2:
            fr_2[i] = fr_2.get(i,0)+1
if len(word_1)==len(word_2):
    for i in range(len(word_1)):
        n = word_1.count(word_1[i])
        m = 0+word_2.count(word_1[i])
        if n != m:
            print("--")
            break"""
word_1=list(input()).sort()
print(word_1)


lis_1 = []
word_1=input()
for i in word_1:
    ind = ord(i)-ord('a')
    lis_1[ind]+=1
lis_2=[]
word_2=input()
for j in word_2:
    ind_2 = ord(j)-ord('a')
    lis_2[ind]+=1