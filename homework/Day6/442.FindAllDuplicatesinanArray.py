class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = set(nums)
        sel = []
        for i in nums:
            if i in arr:
                arr.remove(i)
            else:
                sel.append(i)

        return sel