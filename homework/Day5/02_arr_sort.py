arr=list(map(int, input().split()))
sor = []
for i in range(len(arr)):
    sor.append(min(arr))
    arr.remove(min(arr))

print(sor)