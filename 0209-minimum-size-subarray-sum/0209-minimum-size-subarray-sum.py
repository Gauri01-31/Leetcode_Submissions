class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        j =0
        total =0
        best = n+1
        for i in range(n):
            total += nums[i]
            while total >= target:
                best = min(best, i-j+1)
                total -= nums[j]
                j+=1
        return 0 if best == n+1 else best
        # res = []
        # for i in range(n):
        #     for j in range(i,n):
        #         if sum(nums[i:j+1]) >= target:
        #             res.append(j-i+1)
        # if not res:
        #     return 0
        # return min(res)