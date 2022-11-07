class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        Dict = {}
        for i,n in enumerate(nums):
            if n in Dict and abs(i-Dict[n] <= k):
                return True
            Dict[n] = i
        return False
        