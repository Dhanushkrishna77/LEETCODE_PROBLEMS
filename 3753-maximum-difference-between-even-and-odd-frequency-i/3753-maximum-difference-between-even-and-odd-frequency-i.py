class Solution(object):
    def maxDifference(self, s):
        s_counter=Counter(s)
        max_odd=float('-inf')
        min_even=float('inf')
        for i in s_counter.values():
            if (i%2 !=0) and i>max_odd:
                max_odd=i
            if (i%2 ==0) and i<min_even:
                min_even=i
        return max_odd-min_even