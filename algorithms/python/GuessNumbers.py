class Solution:
    def game(self, guess, answer):
        return len([i for i in range(3) if guess[i] == answer[i]])


if __name__ == '__main__':
    solution = Solution()
    print(solution.game([1,2,3],[1,2,3]))
