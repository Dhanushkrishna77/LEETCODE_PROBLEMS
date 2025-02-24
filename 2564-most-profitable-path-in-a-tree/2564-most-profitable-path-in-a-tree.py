from collections import defaultdict, deque
class Solution(object):
    def mostProfitablePath(self, edges, bob, amount):
       
        n = len(amount)
        self.tree = [[] for i in range(n)]
        self.bob_t = {}
        self.is_open = [False] * n
        profit = -float("inf")
        for u, v in edges:
            self.tree[u].append(v)
            self.tree[v].append(u)
        self.dfs(bob, 0)
        self.is_open = [False] * n
        q = deque([(0, 0, 0)])  

        while q:
            s, t, inc = q.popleft()
            if s not in self.bob_t or t < self.bob_t[s]:
                inc += amount[s]
            elif t == self.bob_t[s]:
                inc += amount[s] // 2
            if len(self.tree[s]) == 1 and s != 0:
                profit = max(inc, profit)
            for node in self.tree[s]:
                if not self.is_open[node]:
                    q.append((node, t + 1, inc))

            self.is_open[s] = True

        return profit

    def dfs(self, s, t):
        self.is_open[s] = True
        self.bob_t[s] = t

        if s == 0:
            return True

        for node in self.tree[s]:
            if not self.is_open[node]:
                if self.dfs(node, t + 1):
                    return True

        self.bob_t.pop(s, None)
        return False