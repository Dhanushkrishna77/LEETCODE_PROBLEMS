
class Solution:
    def numPrimeArrangements(self, n):
        primes = set([
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 
            43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
        ])
        
        a, b = 0, 0
        
        for i in range(1, n + 1):
            if i in primes:
                a += 1
            else:
                b += 1
        
        return (factorial(a) * factorial(b)) % (10**9 + 7)