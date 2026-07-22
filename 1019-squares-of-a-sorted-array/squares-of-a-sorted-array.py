class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #list comprehension
        lst=[i* i for i in nums]
        lst.sort()
        return lst