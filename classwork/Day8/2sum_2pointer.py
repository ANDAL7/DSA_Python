arr = list(map(int,input().split()))
target = int(input())
j = 0
for i in range(len(arr)):
    arr = sorted(arr)
    if arr[i]+arr[-j-1]==target:
        print(arr[i],arr[i+1])
        break
    if sum>target:
        j+=1
    if sum<target:
        continue