class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        lef = 0
        righ = len(numbers)-1
        while lef<righ:
            if numbers[lef]+numbers[righ]==target:
                return lef+1,righ+1
                
            if numbers[lef]+numbers[righ]>target:
                if righ-1==lef:
                    righ = len(numbers)-1
                    lef+=1
                else:
                    righ-=1
            elif numbers[lef]+numbers[righ]<target:
                lef+=1