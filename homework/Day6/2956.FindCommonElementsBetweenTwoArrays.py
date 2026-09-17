class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        arr = [0,0]
        for i in nums1:
            if i in nums2:
                arr[0]+=1
        
        for i in nums2:
            if i in nums1:
                arr[1]+=1
        return arr