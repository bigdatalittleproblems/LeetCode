# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d={}
        maxi=0
        pre=0
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]]=[i]
                maxi=max(maxi,i-pre+1)
            else:
                key=d[s[i]][-1]
                if key>=pre:
                    pre=key+1
                maxi=max(maxi,i-pre+1)
                d[s[i]].append(i)
        return maxi

