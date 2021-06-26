# https://leetcode.com/problems/palindrome-number/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x=str(x)
        solution=str_x[::-1]
        print(solution)
        if str_x==solution:
            return True
        else:
            False