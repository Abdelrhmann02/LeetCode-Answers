class Solution(object):
    def containsDuplicate(self, nums):
        duplicate ={}
        for i in nums:
            if i not in duplicate:
                duplicate[i] = 1
            else:
                return True
        return False