class Solution:
    def getHappyString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def backtrack(path):
            if len(path) == n:
                result.append("".join(path))
                return
            for char in "abc":
                if not path or path[-1] != char:
                    backtrack(path + [char])
        result = []
        backtrack([])
        return result[k - 1] if k <= len(result) else ""