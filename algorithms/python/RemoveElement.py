from typing import List

class Solution:
    # 解1，时间复杂度O(n²)
    def removeElement1(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)

    # 解2，双指针，时间复杂度O(n)    
    def removeElement2(self, nums: List[int], val: int) -> int:
        i = 0
        j = 0
        while j < len(nums):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
                j += 1
            else:
                j += 1
        return i


if __name__ == "__main__":
    solution = Solution()
    print(solution.removeElement2([3,2,2,3],3))
