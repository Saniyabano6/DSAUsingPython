class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        result,power=0,31
        while (n>0):
            result+=(n&1)<<power
            n=n>>1
            power-=1
        return result