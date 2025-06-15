class Solution:
    def maxDiff(self, num):
        s = str(num)

        # -------- Maximum value --------
        for ch in s:
            if ch != '9':
                max_num = int(s.replace(ch, '9'))
                break
        else:
            max_num = num  # already all 9s

        # -------- Minimum value --------
        if s[0] == '1':
            # Replace first non-1 and non-0 digit with 0 (not leading)
            for i in range(1, len(s)):
                if s[i] != '1' and s[i] != '0':
                    ch = s[i]
                    min_num = int(s.replace(ch, '0'))
                    break
            else:
                min_num = num
        else:
            # Replace all occurrences of first digit with '1'
            ch = s[0]
            min_num = int(s.replace(ch, '1'))

        return max_num - min_num