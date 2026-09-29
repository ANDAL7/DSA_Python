class Solution:
    def minSubarraySum(self, arr, k):
        # code here
        fir_sum = sum(arr[:k])
        min_sum = fir_sum
        for i in range(k,len(arr)):
            sec_sum = fir_sum+arr[i]
            sec_sum -=arr[i-k]
            min_sum = min(min_sum,sec_sum)
            fir_sum = sec_sum
        return min_sum