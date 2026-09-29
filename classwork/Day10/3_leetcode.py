class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ind = 0
        out = 0
        set_s=[]
        while ind<len(s):
            if s[ind] not in set_s:
                set_s.append(s[ind])
                ind +=1
                out = max(out,len(set_s))
                if len(s)==len(set_s):
                    return len(s)
            else:
                set_s.pop(0)

        return out