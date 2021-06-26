# https://leetcode.com/problems/reverse-integer/
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ls=[]
        neg=(-1 if x <0 else 1)
        s=str(x*neg)
        print(s)
        returnVal=neg*int(s[::-1])
        if returnVal >=2**31 or returnVal <=-2**31:
            return 0
        return returnVal
