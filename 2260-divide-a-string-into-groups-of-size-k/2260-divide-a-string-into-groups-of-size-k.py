class Solution(object):
    def divideString(self, s, k, fill):
        l=[]
        z=""
        for i in range(len(s)):
            if len(z)!=k:
                z=z+s[i]
            else:
                l.append(z)
                z=""
                z=z+s[i]
        if len(z)==k:
            l.append(z)
        else:
            p=k-len(z)
            z=z+p*(fill)
            l.append(z)
        return l


        