class Solution(object):
    def lenLongestFibSubseq(self, arr):
        n=len(arr)
        dp=[[-1]*n for i in range(n)]

        pos={}

        for i in range(n):
            pos[arr[i]]=i
        for i in range(0,n):
            for j in range(i+1,n):
                dp[i][j]=2
        
        ans=0

        for j in range(n-1,-1,-1):
            for i in range(j-1,-1,-1):
                if (arr[i]+arr[j]) in pos:
                    k=pos[arr[i]+arr[j]]
                    dp[i][j]=max(dp[i][j],dp[j][k]+1)
                    ans=max(ans,dp[i][j])
        
        if ans==2 :
            return 0
        else :
            return ans
                
        """
        :type arr: List[int]
        :rtype: int
        """
        