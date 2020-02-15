class Solution:
    # 解1，时间复杂度O(n)
    def romanToInt(self, s: str) -> int:
        roman_dir = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        sum = roman_dir[s[-1]]
        for i in range(len(s)-1):
            if roman_dir[s[i]] >= roman_dir[s[i+1]]:
                sum += roman_dir[s[i]]
            else:
                sum -= roman_dir[s[i]]
        return sum


if __name__ == "__main__":
    solution = Solution()
    print(solution.romanToInt("MCMXCIV"))
