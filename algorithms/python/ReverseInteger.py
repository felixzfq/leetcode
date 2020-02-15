class Solution:
    # 解1
    def reverse1(self, x: int) -> int:
        if str(x).startswith("-"):
            x = int('-' + str(x)[:0:-1])
        else:
            x = int(str(x)[::-1])
        
        return x if -(2**31) < x < 2**31 - 1 else 0

    # 解2
    def reverse2(self, x: int) -> int:
        s = (x > 0) - (x < 0)
        r = int(str(s*x)[::-1])
        return (s*r) * (r < 2**31)


if __name__ == "__main__":
    solution = Solution()
    print(solution.reverse2(-123))