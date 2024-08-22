class Solution(object):
    def searchInsert(self, nums, target):
        k = 0
        num_finder = 0
        if not nums:
             return 0
         
        for i in range(len(nums)):
            if nums[i] == target:
                num_finder = i
            elif nums[i] < target:
                num_finder += 1

        return num_finder
        
        


solution = Solution()
nums = [1,3,5,6]
target = 8
print(solution.searchInsert(nums, target))
        
         
