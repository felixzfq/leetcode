from typing import List


# 解1，时间复杂度O(n²)
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return [i,j]
        return None
                

# 解2，时间复杂度O(n)
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for n,num in enumerate(nums):
            if (target - num) in d:
                return [d[target - num],n]
            else:
                d[num] = n
        return None


if __name__ == "__main__":
    soultion = Solution2()
    print(soultion.twoSum([2,7,11,15],9))