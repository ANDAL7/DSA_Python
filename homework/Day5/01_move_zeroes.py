arr = list(map(int, input().split()))
ind = 0
for i in arr:
    if i !=0:
        arr[ind] = i
        ind+=1
while ind<len(arr):
    arr[ind] = 0
    ind+=1
print(arr)