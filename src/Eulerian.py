def euleriantab(n, m):
    dp = [[0 for x in range(m + 1)] for y in range(n + 1)]

    # For each row from 1 to n
    for i in range(1, n + 1):

        # For each column from 0 to m
        for j in range(0, m + 1):

            # If i is greater than j
            if (i > j):
                # If j is 0, then make that state as 1.

                if (j == 0):
                    dp[i][j] = 1

                # basic recurrence relation.
                else:
                    dp[i][j] = (((i - j) * dp[i - 1][j - 1]) + ((j + 1) * dp[i - 1][j]))

    return dp[n][m]


def eulerianmem(n, m):
    dp = [[0 for x in range(m + 1)] for y in range(n + 1)]

    if n > m:
        if m == 0:
            dp[n][m] = 1
        else:
            dp[n][m] = ((n - m) * eulerianmem(n - 1, m - 1)) + ((m + 1) * eulerianmem(n - 1, m))

    return dp[n][m]
