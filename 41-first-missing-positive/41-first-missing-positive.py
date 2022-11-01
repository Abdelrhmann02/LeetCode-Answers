class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        Set = set(nums)
        Set = sorted(Set)
        counter = 1
        for i in Set:
            if (i == counter):
                counter += 1
        return counter