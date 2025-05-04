class Solution(object):
    def minDominoRotations(self, tops, bottoms):
        n = len(tops)
        c_top = c_bottom = same = 0
        top = tops[0]
        bottom = bottoms[0]
        for i in range(1, n):
            if tops[i]==bottoms[i]:
                same +=1
            if top!=-1 and tops[i]!=top:
                if bottoms[i]== top:
                    c_top+=1
                else:
                    top = -1
                    c_top = n 
            if bottom!=-1 and bottoms[i]!= bottom:
                if tops[i]== bottom:
                    c_bottom+=1
                else:
                    bottom = -1
                    c_bottom = n 
        t = min(c_top, c_bottom, n-c_top-same if c_top<n else n, n-c_bottom-same if c_bottom<n else n)
        return t if t<n else -1