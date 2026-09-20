def maxSum(self, arr, k):
        # code here
        out = float('-inf')
        n , p = 0,0
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                print(arr[i],arr[j],out)
                if (arr[i]+arr[j])<k and arr[j]-arr[i]>out:
                    print(arr[i],arr[j],out)
                    out = arr[j]-arr[i]
                    n = arr[i]
                    p = arr[j]
        
        if n==0 and p==0:
            return -1,-1
        else:
            return n,p
print(maxSum(1,[1, 2, 3, 4, 5], 7))