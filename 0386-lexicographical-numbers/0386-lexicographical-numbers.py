class Solution:
    def lexicalOrder(self, n):
        return [int(j) for j in sorted([str(i+1) for i in range(n)])]