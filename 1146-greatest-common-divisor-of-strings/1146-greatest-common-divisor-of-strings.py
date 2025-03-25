class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if str1 + str2 != str2 + str1:
            return ""
        def gcd(val1, val2):
            while val2:
                val1, val2 = val2, val1 % val2
            return val1

        gcd_length = gcd(len(str1), len(str2))
        return str1[:gcd_length]





      
        