class Solution:
    def prefixAvg(self, arr):
        # code here
        arr_1=[]
        sum_1 = 0
        for i in range(len(arr)):
            sum_1+=arr[i]
            arr_1.append(sum_1//(i+1))
            
        return arr_1