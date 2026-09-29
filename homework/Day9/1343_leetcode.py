class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        val = 0
        sum_value=sum(arr[:k])
        for i in range(k,len(arr)+1):
            avg = sum_value/k
            if avg>=threshold:
                val+=1
            if i<len(arr):
                sum_value-=arr[i-k]
                sum_value+=arr[i]
        return val