class Eulerian:
    dp = None

    def __init__(self, n, m):
        self.dp = [[0 for x in range(m + 1)] for y in range(n + 1)]

    def euleriantab(self, n, m):
        # For each row from 1 to n
        for i in range(1, n + 1):

            # For each column from 0 to m
            for j in range(0, m + 1):

                # If i is greater than j
                if i > j:
                    # If j is 0, then make that state as 1.

                    if j == 0:
                        self.dp[i][j] = 1

                    # basic recurrence relation.
                    else:
                        self.dp[i][j] = (((i - j) * self.dp[i - 1][j - 1]) + ((j + 1) * self.dp[i - 1][j]))

        return self.dp[n][m]

    def eulerianmem(self, n, m):
        if self.dp[n][m] != 0:
            return self.dp[n][m]
        if n > m:
            if m == 0:
                self.dp[n][m] = 1
            else:
                self.dp[n][m] = ((n - m) * self.eulerianmem(n - 1, m - 1)) + ((m + 1) * self.eulerianmem(n - 1, m))
        return self.dp[n][m]
