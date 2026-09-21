class Solution:
    def maxSum(self, arr, k):
        arr.sort()

        lf = 0
        rgh = len(arr) - 1

        sum = float('-inf')
        diff = float('-inf')
        n,p=-1,-1

        while lf < rgh:
            total = arr[lf] + arr[rgh]

            if total < k:
                diff_1 = abs(arr[lf] - arr[rgh])

                if total > sum or (total == sum and diff_1 > diff):
                    sum = total
                    diff = diff_1
                    n,p=arr[lf],arr[rgh]

                lf += 1

            else:
                rgh -= 1

        return n,p