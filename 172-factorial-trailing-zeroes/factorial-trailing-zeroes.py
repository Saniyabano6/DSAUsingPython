class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        fact=1
        for i in range(2,n+1):
            fact*=i
        count=0
        s=str(fact)[::-1]
        for i in s:
            if i=='0':
                count+=1
            else:
                break 
        return count
