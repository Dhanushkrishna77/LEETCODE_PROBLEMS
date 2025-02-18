class Solution(object):
    def candy(self, ratings):
        decending = -1
        hold = None
        i = 0
        c = 0
        old = 0
        while i<len(ratings):
            if decending !=-1:
                if i==len(ratings)-1 or ratings[i]==ratings[i+1]:
                    c+=max(hold, 1+ i-decending)+ sum(range(i-decending+1))
                    old = 0
                    decending =-1
                elif ratings[i] <ratings[i+1]:
                    c+=max(hold, 1+ i-decending)+ sum(range(i-decending+1))
                    old = 1
                    decending =-1
            elif i==len(ratings)-1 or ratings[i] <ratings[i+1]:
                old+=1
                c+=old
            elif ratings[i]==ratings[i+1]:
                old+= 1
                c+= old
                old = 0
            else:
                old+=1
                hold = old
                decending = i
            i+=1
        return c
