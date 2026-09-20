class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            dif = target-nums[i]
            if (dif in nums) and i!=nums.index(dif):
                return i,nums.index(dif)
        