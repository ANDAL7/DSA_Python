class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        arr=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                n = 0
                for k in range(len(nums)):
                    u = len(nums)+(-n-1)
                    if nums[i]+nums[j]+nums[k]+nums[-n-1]==target and len({u,i,j,k})==4:
                        sor = sorted([nums[i],nums[j],nums[k],nums[-n-1]])
                        if sor in arr:
                            continue
                        else:
                            arr.append(sor)
                    n+=1
        return arr
    """one of the way but not passes all the test cases"""