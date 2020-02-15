# 解1，时间复杂度O(n²)
class Solution1:
    def removeDuplicates(self, nums: list) -> int:
        for i in range(len(nums)-1,0,-1):
            if nums[i] == nums[i-1]:
                 nums.pop(i)                   
        return len(nums)


# 解2，时间复杂度O(n)
class Solution2:
    def removeDuplicates(self, nums: list) -> int:
        i = 0
        for j in range(0,len(nums)):
            if nums[i] != nums[j]:  
                nums[i+1] = nums[j]
                i += 1
        return i+1 if nums else 0