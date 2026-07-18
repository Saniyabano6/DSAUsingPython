class Solution(object):
    def lengthOfLastWord(self, s):
        list=s.split()
        if len(list)==0:
            return 0
        return len(list[-1])
        