class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}

        def func(i, j):
            if i == len(word1):
                return len(word2) - j

            if j == len(word2):
                return len(word1) - i

            if (i, j) in memo:
                return memo[(i, j)]

            if word1[i] == word2[j]:
                ans = func(i + 1, j + 1)
            else:
                insert = func(i, j + 1)
                delete = func(i + 1, j)
                replace = func(i + 1, j + 1)

                ans = 1 + min(insert, delete, replace)

            memo[(i, j)] = ans
            return ans

        return func(0, 0)