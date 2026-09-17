arr = list(map(int, input().split()))
arr_Set = set(arr)
if len(arr)==len(arr_Set):
    print(False)
else:
    print(True)