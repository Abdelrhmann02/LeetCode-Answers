class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Dict = {}
        for index,num in enumerate(nums):
            remaining = target - num
            if remaining in Dict:
                return [Dict[remaining],index]
            else:
                Dict[num] = index