class Solution(object):
    def isMatch(self, s, p):
            # Initialize DP table
        n, m = len(s), len(p)
        dp = [[False] * (m+1) for _ in range(n+1)]
        dp[0][0] = True

        # Fill in first row (for pattern starting with *)
        for j in range(1, m+1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]

        # Fill in DP table
        for i in range(1, n+1):
            for j in range(1, m+1):
                if s[i-1] == p[j-1] or p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-2] or (dp[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == '.'))
        
        return dp[n][m]