class Solution:
    # 解1,时间复杂度O(n)
    def isPalindrome1(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

    # 解2，时间复杂度O(log10(n))
    def isPalindrome2(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        revertedNumber = 0
        while x > revertedNumber:
            revertedNumber = x % 10 + revertedNumber * 10
            x //= 10

        return (x == revertedNumber // 10) or (x == revertedNumber)

if __name__ == "__main__":
    solution = Solution()
    print(solution.isPalindrome2(11))