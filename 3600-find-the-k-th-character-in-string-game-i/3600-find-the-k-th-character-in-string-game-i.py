class Solution(object):
    def kthCharacter(self, k):
        initial=['a']
        while len(initial)<k:
            for i in range(len(initial)):
                initial.append(chr(1+ord(initial[i])))
        return initial[k-1]