class Solution(object):
    def longestSubsequence(self, s, k):
        z = 0
        coff = 1
        for i in range(len(s)-1, -1, -1):
            if s[i]=='1':
                if coff<=k:
                    k-=coff
                    z+=1
            else:
                z+=1
            coff*=2
        return z