class Solution(object):
    def countGoodArrays(self, n, m, k):
        MOD = 10**9 + 7
        fact = [1] * (n)
        inv = [1] * (n)

        for i in range(1, n):
            fact[i] = fact[i - 1] * i % MOD

        inv[n - 1] = pow(fact[n - 1], MOD - 2, MOD)
        for i in range(n - 2, -1, -1):
            inv[i] = inv[i + 1] * (i + 1) % MOD

        def comb(a, b):
            if b < 0 or b > a:
                return 0
            return fact[a] * inv[b] % MOD * inv[a - b] % MOD

        power = pow(m - 1, n - 1 - k, MOD)
        return m * comb(n - 1, k) % MOD * power % MOD
