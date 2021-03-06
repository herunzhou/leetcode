class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0] == "0":
            return 0

        # dp[i] = # of ways to decode at ith letter
        dp = [0 for x in range(len(s) + 1)]
        dp[0] = 1
        dp[1] = 1

        # 226
        for i in range(2, len(s) + 1):
            if 0 < int(s[i - 1: i]) <= 9:
                dp[i] += dp[i - 1]
            if 10 <= int(s[i - 2: i]) <= 26:
                dp[i] += dp[i - 2]

        return dp[-1]
