class Solution:
    def maximumAmount(self, coins):
        n, m = len(coins), len(coins[0])
        self.dp = [[[float('-inf')] * 3 for _ in range(m)] for _ in range(n)]

        def solve(i, j, neut):
            if i >= n or j >= m:
                return float('-inf')

            if i == n - 1 and j == m - 1:
                if coins[i][j] < 0 and neut > 0:
                    return 0
                return coins[i][j]

            if self.dp[i][j][neut] != float('-inf'):
                return self.dp[i][j][neut]

            down = float('-inf')
            right = float('-inf')

            if i + 1 < n:
                if coins[i][j] >= 0:
                    nxt = solve(i + 1, j, neut)
                    if nxt != float('-inf'):
                        down = coins[i][j] + nxt
                else:
                    take = float('-inf')
                    nxt = solve(i + 1, j, neut)
                    if nxt != float('-inf'):
                        take = coins[i][j] + nxt

                    nottake = float('-inf')
                    if neut > 0:
                        nottake = solve(i + 1, j, neut - 1)

                    down = max(take, nottake)

            if j + 1 < m:
                if coins[i][j] >= 0:
                    nxt = solve(i, j + 1, neut)
                    if nxt != float('-inf'):
                        right = coins[i][j] + nxt
                else:
                    take = float('-inf')
                    nxt = solve(i, j + 1, neut)
                    if nxt != float('-inf'):
                        take = coins[i][j] + nxt

                    nottake = float('-inf')
                    if neut > 0:
                        nottake = solve(i, j + 1, neut - 1)

                    right = max(take, nottake)

            self.dp[i][j][neut] = max(down, right)
            return self.dp[i][j][neut]

        return solve(0, 0, 2)