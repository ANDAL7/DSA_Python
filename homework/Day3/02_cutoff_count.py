test_cases = int(input(""))
for i in range(test_cases):
    n , c = map(int,input().split())
    arr = list(map(int,input().split()))
    arr_1 = []
    for j in arr:
        if j>=c:
            arr_1.append(j)

    print("Total : ",len(arr_1))
    print(*arr_1,sep=",")
    print(" are atleast ",c)