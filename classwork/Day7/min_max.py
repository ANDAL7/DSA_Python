arr = list(map(int, input().split()))
a = [0,5,10,15]
ele = 0
print("Running maximums : ")
for i in arr:
    if ele >i and (ele in a):
        print(ele,end = " ")
    elif ele<i and (ele in a):
        ele  = i
        print(ele,end = " ")
    else:
        continue

print("\nRunning minimums : ")
ele = arr[0]
for i in arr:
    if ele <=i and (ele in a):
        print(ele,end = " ")
    elif ele>i and (ele in a):
        ele  = i
        print(ele,end = " ")
    else:
        continue