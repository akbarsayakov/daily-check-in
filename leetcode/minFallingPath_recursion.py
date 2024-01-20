class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        N = len(matrix)
        res = float('inf')
        cache = {}

        def dfs(r, c):
            if r == N:
                return 0
            if c < 0 or c == N:
                return float('inf')

            if (r, c) in cache:
                return cache[(r, c)]

            res = matrix[r][c] + min(
                dfs(r + 1, c - 1),
                dfs(r + 1, c),
                dfs(r + 1, c + 1)
            )
            cache[(r, c)] = res
            return res
        for c in range(N):
            res = min(res, dfs(0, c))
        
        return res