class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0] *n for _ in range(n)]
        t ,b, l, r = 0,n-1,0,n-1
        num = 1

        while t<=b and l<=r:
            for j in range(l, r + 1):
                matrix[t][j] = num
                num += 1
            t += 1

            for i in range(t, b+ 1):
                matrix[i][r] = num
                num += 1
            r -= 1
            if t<= b:
                for j in range(r, l - 1, -1):
                    matrix[b][j] = num
                    num += 1
                b -= 1

            if l<= r:
                for i in range(b, t - 1, -1):
                    matrix[i][l] = num
                    num += 1
                l += 1

        return matrix
        