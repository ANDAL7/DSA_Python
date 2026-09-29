class Solution:
    def removeDuplicates(self, s):
        # code here
        res = [s[0]]
        for i in range(len(s)-1):
            if s[i]!=s[i+1]:
                res.append(s[i+1])
        k = "".join(res)
        return k