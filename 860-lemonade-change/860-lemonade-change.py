class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five = ten = 0
        for i in bills:
            if i == 5:
                five+=1
            elif i == 10:
                if not five: return False
                five-=1
                ten +=1
            else:
                if five and ten:
                    ten-=1
                    five-=1
                elif five>=3:
                    five-=3
                else:
                    return False
        return True
        