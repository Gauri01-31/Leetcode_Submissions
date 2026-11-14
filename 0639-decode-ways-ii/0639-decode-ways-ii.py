class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10**9 + 7
        def one(c):
            if c == '*':
                return 9
            return 0 if c == '0' else 1
        def two(a, b):
            if a == '*' and b == '*':
                return 15
            if a == '*':
                return 2 if b <= '6' else 1
            if b == '*':
                if a == '1':
                    return 9
                if a == '2':
                    return 6
                return 0
            return 1 if 10 <= int(a + b) <= 26 else 0
        prev2, prev1 = 1, one(s[0])
        for i in range(2, len(s) + 1):
            cur = (prev1 * one(s[i - 1]) + prev2 * two(s[i - 2], s[i - 1])) % MOD
            prev2, prev1 = prev1, cur
        return prev1