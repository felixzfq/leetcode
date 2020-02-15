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

