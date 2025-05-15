class Solution(object):
    def getLongestSubsequence(self, words, groups):
        y=[words[0]]
        for i in range(1,len(words)):
            if groups[i-1]!=groups[i]:
                y.append(words[i])
        return y