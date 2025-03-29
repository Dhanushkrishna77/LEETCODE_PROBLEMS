class Solution(object):
    def maximumScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        n = len(nums)
        factor=[0]*n
        scores=[]
        for i in range(n):
            score=self.prime_factors_count(nums[i])
            factor[i]=score
            #scores.append([score, nums[i], i])


        
        #scores.sort(key=lambda x: (-x[1]))

        result = 1
        stack = []
        left_bounds = [-1] * n
        for idx in range(n):
            while stack and factor[stack[-1]] < factor[idx]:
                stack.pop()
            left_bounds[idx] = stack[-1] if stack else -1
            stack.append(idx)

        # 使用单调栈找到每个因子的右边界
        stack = []
        right_bounds = [n] * n
        for idx in range(n-1, -1, -1):
            while stack and factor[stack[-1]] <= factor[idx]:
                stack.pop()
            right_bounds[idx] = stack[-1] if stack else n
            stack.append(idx)

        # 使用左右边界计算每个元素的times
        times = [(right_bounds[i] - i) * (i - left_bounds[i]) for i in range(n)]
        pairs = sorted(zip(nums, times), key=lambda x: -x[0])

        result = 1
        for num, time in pairs:
            use_times = min(k, time)
            result = (result * self.quick_pow(num, use_times, MOD)) % MOD
            k -= use_times
            if k == 0:
                return result 
                break 

            
            
    def prime_factors_count(self,n):
        j, res = 2, []
        while n > 1:
            for i in range(j, int(sqrt(n + 0.05)) + 1):
                if n % i == 0:
                    n //= i
                    j = i
                    res.append(i)
                    break
            else:
                if n > 1:
                    res.append(n)
                    break

        return len(set(res))
    def quick_pow(self,a, b, MOD):
        result = 1
        while b:
            if b & 1:
                result = (result * a) % MOD
            a = (a * a) % MOD
            b >>= 1
        return result
        