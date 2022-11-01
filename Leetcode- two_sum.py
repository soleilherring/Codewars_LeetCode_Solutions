class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
# PREP
# P: parameters - nums(list), target(integer)
# R: return - 2 indices of num in nums that sum is target
# E: example - Input: nums = [2,7,11,15], target = 9; Output: [0,1]
# P: pseudocode:
# make guard clause for empty target /num etc
# create new list
# create first for loop for current element
# create second for loop for other elements we are checking
#   if the two elements add up to the target, append those indices to the list
# return the new list 

        for i in range(len(nums)-1): 
            for j in range(i+1,len(nums)): 
                if nums[i] + nums[j] == target:            
                    return  [i,j]