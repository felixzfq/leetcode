from typing import List


# 解1，时间复杂度O(n)，空间复杂度O(1)
class Solution1:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0,len(numbers)-1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1
        return []


# 解2，时间复杂度O(nlogn)，空间复杂度O(1)
class Solution2:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for n in range(len(numbers)):
            l,r = n + 1,len(numbers) - 1
            tmp = target - numbers[n]
            while l <= r :
                mid = l + (r - l) // 2
                if numbers[mid] == tmp:
                    return [n + 1,mid + 1]
                elif numbers[mid] < tmp:
                    l = mid + 1
                else:
                    r = mid - 1
        return []


if __name__ == "__main__":
    soultion = Solution2()
    print(soultion.twoSum([1,2,3,4,4,9,56,90],8))
