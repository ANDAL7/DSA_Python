class Solution:
    def maxSubarraySum(self, arr, k):
        # code here
        fir_sum = sum(arr[:k])
        max_sum = fir_sum
        for i in range(k,len(arr)):
            sec_sum = fir_sum+arr[i]
            sec_sum -=arr[i-k]
            max_sum = max(max_sum,sec_sum)
            fir_sum = sec_sum
        return max_sum