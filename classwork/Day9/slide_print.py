class Solution:
    def minSubarraySum(self, arr, k):
        # code here
        for i in range(len(arr)-k+1):
            arr_1 =[]
            for j in range(i,i+k):
                arr_1.append(arr[j])
            print(arr_1)