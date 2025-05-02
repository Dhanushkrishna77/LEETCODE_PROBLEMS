class Solution(object):
    def pushDominoes(self, dominoes):
        force = N = len(dominoes)
        tmp = 0
        ans = [0] * N
        for i in range(N):
            if dominoes[i] == 'R':
                tmp = force
            if dominoes[i] == 'L':
                tmp = 0
            ans[i] += max(tmp, 0)
            tmp -= 1
        tmp = 0
        for i in range(N-1, -1, -1):
            if dominoes[i] == 'L':
                tmp = -force
            if dominoes[i] == 'R':
                tmp = 0
            ans[i] += min(tmp, 0)
            tmp += 1
        return ''.join([ 'R' if n>0 else 'L' if n<0 else '.' for n in ans])
        