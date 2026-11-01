class Solution(object):
    def minMergedInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        res = float('inf')
        for i in range(0,n,2):
            merge = int(str(nums[i]) + str(nums[i+1]))
            res = min(merge,res)
        return res