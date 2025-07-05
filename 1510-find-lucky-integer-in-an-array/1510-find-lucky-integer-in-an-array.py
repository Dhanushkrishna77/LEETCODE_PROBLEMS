class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        d={}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        res=[]
        for key,val in d.items():
            if key == val:
                res.append(val)
        if res:
            lar = res[0]
            for i in res:
                if i > lar:
                    lar=i 
            return (lar)
        else:
            return (-1)


obj = Solution()
print(obj.findLucky([2,2,3,4]))
print(obj.findLucky([1,2,2,3,3,3]))
print(obj.findLucky([2,2,2,3,3]))