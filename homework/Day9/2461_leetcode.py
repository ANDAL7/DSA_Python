class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        fr={}
        sum_1=0
        for i in range(k):
            fr[nums[i]]=fr.get(nums[i],0)+1
            sum_1+=nums[i]
        val=0
        for j in range(k,len(nums)+1):
            if len(fr) == k:
                val = max(val, sum_1)
            if j==len(nums):
                break
            sum_1 -= nums[j-k]
            sum_1+=nums[j]
            fr[nums[j]]=fr.get(nums[j],0)+1
            fr[nums[j-k]]-=1
            if fr[nums[j-k]] == 0:
                del fr[nums[j-k]]
        return val