arr = list(map(int, input().split()))
max_1 = arr[0]
max_2 = arr[0]
for i in arr:
    if max_1<i:
        max_1 = i
    if max_2<i and i!=max_1:
        max_2 = i

print("First largest element is:", max_1)
print("Second largest element is:", max_2)