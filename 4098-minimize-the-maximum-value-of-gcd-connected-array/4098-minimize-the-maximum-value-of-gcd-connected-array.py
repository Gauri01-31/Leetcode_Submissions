class Solution(object):
    def minimumMaxValue(self, n, index, value):
        """
        :type n: int
        :type index: int
        :type value: int
        :rtype: int
        """
        if n == 1:
             return n
        if value == 1:
            return -1
        p = value
        d = 2
        while d * d <= value:
            if value % d == 0:
                p = d
                break
            d += 1
        if value % 2 == 0:
            left_cap = value // 2 - 1
        else:
            left_cap = (value - p) // 2
        if index > left_cap:
            return -1

        k = n - 1 - index
        if k == 0:
            return value
        if value % 2 == 0:
            return value + 2 * k
        return value + p + 2 * (k - 1)
        