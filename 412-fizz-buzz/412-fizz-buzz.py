class Solution(object):
    def fizzBuzz(self, n):
        final = []
        for i in range(1,n+1):
            answer=""
            if(i%3 == 0):
                answer+="Fizz"
            if(i%5 == 0):
                answer+="Buzz"
            if not answer:
                answer+=str(i)
            final.append(answer)
        return final
        
        """
        :type n: int
        :rtype: List[str]
        """
        