"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
"""


class Solution:
    def reverse(self, x: int) -> int:
        if str(x).startswith("-"):
            x = int('-' + str(x)[:0:-1])
        else:
            x = int(str(x)[::-1])
        
        return x if -(2**31) < x < 2**31 - 1 else 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.reverse(123))