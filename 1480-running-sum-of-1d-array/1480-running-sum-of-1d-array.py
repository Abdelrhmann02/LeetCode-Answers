class Solution(object):
    def runningSum(self, nums):
        currsum = 0
        answer =[]
        for i in nums:
            currsum+= i
            answer.append(currsum)
        return answer

        """
        :type nums: List[int]
        :rtype: List[int]
        """