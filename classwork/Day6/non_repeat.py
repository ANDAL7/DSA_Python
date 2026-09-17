arr = list(map(int, input().split()))
frequency = {}
for i in arr:
    frequency[i] = frequency.get(i, 0) + 1
for i,j in frequency.items():
    if j == 1:
        print(i," : ",j)
        break