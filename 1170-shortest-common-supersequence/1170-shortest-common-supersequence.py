class Solution:
    def shortestCommonSupersequence(self, str1, str2):
        len1, len2 = len(str1), len(str2)
        table = [[0] * (len2 + 1) for _ in range(len1 + 1)]

        for x in range(1, len1 + 1):
            for y in range(1, len2 + 1):
                if str1[x - 1] == str2[y - 1]:
                    table[x][y] = table[x - 1][y - 1] + 1
                else:
                    table[x][y] = max(table[x - 1][y], table[x][y - 1])

        x, y = len1, len2
        sequence = []

        while x > 0 or y > 0:
            if x > 0 and y > 0 and str1[x - 1] == str2[y - 1]:
                sequence.append(str1[x - 1])
                x -= 1
                y -= 1
            elif y > 0 and (x == 0 or table[x][y - 1] >= table[x - 1][y]):
                sequence.append(str2[y - 1])
                y -= 1
            else:
                sequence.append(str1[x - 1])
                x -= 1

        return "".join(reversed(sequence))