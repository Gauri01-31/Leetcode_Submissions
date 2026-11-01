class Solution(object):
    def minOperations(self, nums, locked, k):
        """
        :type nums: List[int]
        :type locked: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)

        # indices that must be unlocked
        need = [False] * n
        mx = 0
        for i in range(n - 1):
            mx = max(mx, nums[i])
            if mx != i + 1:          # bad boundary between i and i+1
                need[i] = True
                need[i + 1] = True

        unlocks = sum(1 for i in range(n) if need[i] and locked[i] == 1)
        if unlocks > k:
            return -1

        # count inversions with a Fenwick tree
        tree = [0] * (n + 1)
        inv = 0
        for i in range(n - 1, -1, -1):
            # count smaller values already seen to the right
            j = nums[i] - 1
            while j > 0:
                inv += tree[j]
                j -= j & -j
            j = nums[i]
            while j <= n:
                tree[j] += 1
                j += j & -j

        return inv + unlocks