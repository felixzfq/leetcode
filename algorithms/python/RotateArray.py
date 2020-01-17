"""
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

示例 1:
输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/roman-to-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# 解1,数组拼接，空间复杂度O(n)
class Solution1:
    def rotate(self, nums: list, k: int) -> None:
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        return nums


# 解2，3次翻转，空间复杂度O(1)
class Solution2:
    def rotate(self, nums: list, k: int) -> None:
        k, start, end = k % len(nums), 0, len(nums) - 1
        self._reverse(nums, start, end - k)
        self._reverse(nums, end-k+1, end)
        self._reverse(nums, start, end)

    def _reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

