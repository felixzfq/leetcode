'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。
'''


from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for n in range(len(nums)):
            p1 = n
            p2 = len(nums) - 1
            while p1 < p2:
                if nums[p1] + nums[p2] == target:
                    return [p1,p2]
                else:
                    p2 -= 1



if __name__ == "__main__":
    soultion = Solution()
    print(soultion.twoSum([3,2,4],6))