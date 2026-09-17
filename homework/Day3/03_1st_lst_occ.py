test_cases = int(input(""))
for i in range(test_cases):
    n , c = map(int,input().split())
    arr = list(map(int,input().split()))
    fir = 0
    las = 0
    for j in arr:
        if j==c:
            fir += arr.index(j)
            break

    arr_1 = arr[::-1]
    for k in arr_1:
        if k==c:
            las += (len(arr)-1)-(arr_1.index(k))
            break
    print("First Occurrence : ",fir)
    print("Last Occurrence : ",las)