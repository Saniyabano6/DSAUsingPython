class Solution(object):
    def twoSum(self, nums, target):
        d = {}  # Initialize the dictionary
        
        # Build the hash map
        for i in range(len(nums)):
            d[nums[i]] = i
            
        # Check for the complement
        for i in range(len(nums)):
            need = target - nums[i]
            
            if need in d and d[need] != i:
                return [i, d[need]]