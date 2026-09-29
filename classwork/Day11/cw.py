nums=list(map(int,input().split()))
target=int(input())
lef = 0
val=float('inf')
righ = len(nums)-1
arr=[]
while lef<righ:
    if nums[lef]+nums[righ]>target:
        if val>nums[lef]+nums[righ]:
            val=nums[lef]+nums[righ]
            arr=[nums[lef],nums[righ]]
        righ -=1
    elif nums[lef]+nums[righ]<target:
        lef+=1
    else:
        lef+=1
print(arr)