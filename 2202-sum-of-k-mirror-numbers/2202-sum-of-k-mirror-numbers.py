class Solution:
    def kMirror(self, k, n):
        def is_pal_10(x):
            orig, rev = x, 0
            while x:
                rev = rev * 10 + x % 10
                x //= 10
            return rev == orig

        ans = 0
        found = 0
        length = 1

        while found < n:
            half = (length + 1) // 2
            start = 1 if half == 1 else k ** (half - 1)
            end = k ** half

            for prefix in range(start, end):
                # build the base-k palindrome from the prefix
                pal = prefix
                t = prefix // k if (length % 2) else prefix
                while t:
                    pal = pal * k + (t % k)
                    t //= k

                # if its decimal form is also a palindrome, include it
                if is_pal_10(pal):
                    ans += pal
                    found += 1
                    if found == n:
                        return ans

            length += 1

        return ans