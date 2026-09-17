test_cases = int(input())
for i in range(test_cases):
    arr = input().split()
    arr_set = set(arr)
    if len(arr)==len(arr_set):
        print("YES")
    else:
        print("NO")