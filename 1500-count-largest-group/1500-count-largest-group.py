class Solution(object):
    def countLargestGroup(self, n):
        res = []
        for i in range(1, n+1):
            res.append(sum(int(x) for x in str(i)))      
        c = collections.Counter(res)
        x = [i for i in c.values() if i == max(c.values())]
        return len(x)
    
    