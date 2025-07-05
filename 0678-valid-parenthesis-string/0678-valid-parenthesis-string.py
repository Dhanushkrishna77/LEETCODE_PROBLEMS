class Solution:
    def checkValidString(self, s):
        while s != s.replace("()", ""):
            s = s.replace("()", "")
        queue = []
        for i in range(len(s)):
            if s[i] in ["(", "*"]:
                queue.append(1)
            else:
                if queue:
                    queue.pop()
                else:
                    return False
        queue = []
        for i in range(len(s) - 1, -1, -1):
            if s[i] in [")", "*"]:
                queue.append(1)
            else:
                if queue:
                    queue.pop()
                else:
                    return False
        return True