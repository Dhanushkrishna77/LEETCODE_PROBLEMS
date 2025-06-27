class Solution:
    def longestSubsequenceRepeatedK(self, s, k):
        # seq * k is a subsequent 
        counter = Counter(s)
        s = ''.join([c for c in s if counter[c] >= k])
        
        def is_subsequence(t):
            # determine that t is a subsequence of s
            i = j = 0
            while i < len(t) and j < len(s):
                if s[j] == t[i]:
                    i += 1
                    j += 1
                    
                else:
                    j += 1
            return i == len(t) and j <= len(s)
        
        def get_sequence(seqs, length):
            # if length > len(s) // k + 2:
            #     return seqs
            
            rslt = {}
            for seq, index in seqs.items():
                visited = set()
                i = index + 1
                while i < len(s):
                    newseq = (seq[:] + s[i])
                    if newseq not in visited:
                        if is_subsequence(newseq * k):
                            rslt[newseq] = i
                        visited.add(newseq)
                    i += 1
            
            if rslt:
                return get_sequence(rslt, length + 1)
            else:
                return seqs
        
        seqs = get_sequence({'': -1}, 0)
        # sort and return the biggest
        return sorted(list(seqs.keys()), key=lambda x: (len(x), x))[-1]