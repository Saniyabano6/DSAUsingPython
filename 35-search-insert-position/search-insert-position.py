class Solution(object):
    def searchInsert(self, nums, target):
        i=0
        while (i<len(nums) and target >=nums[i]):
            if (nums[i]==target):
                return i
            i+=1
        return i 
        