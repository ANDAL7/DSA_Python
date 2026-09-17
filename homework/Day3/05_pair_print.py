test_cases = int(input(""))
for i in range(test_cases):
    n = int(input())
    arr = list(map(int,input().split()))
    for j in range(len(arr)):
        for k in range((len(arr))):
            if j<k:
                print("(",arr[j],",",arr[k],")")
    