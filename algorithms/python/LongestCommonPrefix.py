from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        prefix = strs[0]
        for i in range(1,len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[:-1]
                if prefix == 0:
                    return ""
        return prefix


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestCommonPrefix(["c","acc","ccc"]))
    
