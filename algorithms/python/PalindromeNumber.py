"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/roman-to-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


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