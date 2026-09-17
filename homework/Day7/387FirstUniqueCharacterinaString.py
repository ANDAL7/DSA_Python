class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        fr ={}
        for x in s:
            fr[x] = fr.get(x,0)+1
        for i in range(len(s)):
            if fr[s[i]]==1:
                return i
        return -1