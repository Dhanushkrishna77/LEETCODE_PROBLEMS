class Solution:
    def minMaxDifference(self, num):
        maxx = num
        for d in str(maxx):
            if d != "9":
                maxx = int(str(maxx).replace(d,"9"))
                break
        minn = int(str(num).replace(str(num)[0],"0"))
        return maxx - minn

        