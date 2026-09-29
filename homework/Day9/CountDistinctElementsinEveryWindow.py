class Solution:
    def countDistinct(self, arr, k):
        # code here
        arr_1 = []
        ele = arr[:k]
        righ = k
        while righ <= len(arr):
            arr_1.append(len(set(ele)))
            if righ == len(arr):
                break
            del ele[0]
            ele.append(arr[righ])
            righ+=1
        return arr_1
    """not passes all the test cases"""