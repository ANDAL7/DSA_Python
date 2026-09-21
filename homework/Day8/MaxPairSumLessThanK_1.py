class Solution:
    def maxSum(self, arr, k):
        # code here
        out = float('-inf')
        n , p = -1,-1
        high = float('-inf')
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if arr[i]+arr[j]<k and arr[i]+arr[j]>high:
                    high = arr[i]+arr[j]
                    out = abs(arr[i]-arr[j])
                    n = arr[i]
                    p = arr[j]
                elif abs(arr[i]-arr[j])>out and arr[i]+arr[j]==high:
                    out = abs(arr[i]-arr[j])
                    n = arr[i]
                    p = arr[j]
            
        sor=[n,p]
        return sorted(sor)
    """this is from geeks for geeks and this is O(n^)"""