class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MaxSum = CurrSum = nums[0]
        for i in nums[1:]:
            CurrSum = max(i,CurrSum+i)
            MaxSum = max(MaxSum,CurrSum)
        return MaxSum