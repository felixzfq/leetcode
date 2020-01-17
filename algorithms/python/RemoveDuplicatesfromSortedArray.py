"""
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/roman-to-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

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