class Solution:
    def solve(self, nums):
        nums = sorted(nums)
        differences = []
        for i in range(len(nums)-1):
            d = nums[i+1] - nums[i] 
            differences.append(d)
        if len(set(differences)) == 1:
            return True    
        else:
            return False 