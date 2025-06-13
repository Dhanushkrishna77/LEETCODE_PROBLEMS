
class Solution:

    def minSum(self, nums1, nums2):
        s1 = s2 = 0
        c1 = c2 = 0

        for num in nums1:
            if num == 0:
                c1 += 1
            else:
                s1 += num
        s1 += c1
        for num in nums2:
            if num == 0:
                c2 += 1
            else:
                s2 += num
        s2 += c2

        if (s1 < s2 and c1 == 0) or (s2 < s1 and c2 == 0):
            return -1
        return max(s1, s2)