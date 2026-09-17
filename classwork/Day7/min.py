arr = list(map(int, input().split()))
ele = arr[0]
for i in arr:
    if ele <=i:
        print(ele,end = " ")
    elif ele>i:
        ele  = i
        print(ele,end = " ")
    else:
        continue