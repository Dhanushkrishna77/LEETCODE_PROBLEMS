class Solution:
    def mergeAlternately(self, word1, word2):
        return ''.join(a+b for a, b in zip(word1, word2)) + word1[len(word2):] + word2[len(word1):]