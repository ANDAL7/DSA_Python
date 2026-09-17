arr = list(map(int, input().split()))
min_ele = arr[0]
max_ele = arr[0]
for i in arr:
    if min_ele > i:
        min_ele = i
    if max_ele < i:
        max_ele = i

print("Minimum element is:", min_ele)
print("Maximum element is:", max_ele)