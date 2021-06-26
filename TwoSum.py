# https://leetcode.com/problems/two-sum/
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        print(nums)
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if i==j:
                    pass
                else:
                    checkval=nums[i]+nums[j]
                    if checkval==target:
                        print("i is: {}".format(i))
                        print("j is: {}".format(j))
                        return([i,j])
                    else:
                        pass
