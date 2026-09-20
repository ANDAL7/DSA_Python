arr = list(map(int, input().split()))
ta = int(input())
if ta in arr:
    print("first occurence : ",arr.index(ta))
    for i in range(len(arr)):
        if arr[-i-1]==ta:
            lst = len(arr)-i-1
            print("last_occurence : ",lst)
            break
else:
    print("first occurence : -1")
    print("last_occurence : -1")