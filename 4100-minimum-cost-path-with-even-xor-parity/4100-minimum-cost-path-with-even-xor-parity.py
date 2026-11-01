class Solution(object):
    def minActivationCost(self, edges, values):
        """
        :type edges: List[List[int]]
        :type values: List[int]
        :rtype: int
        """
        n = len(values)
        INF = float('inf')
        b = [bin(v).count('1') & 1 for v in values]

        # for each node: two smallest edge costs to neighbors with b=0 and b=1
        best = [[[INF, INF], [INF, INF]] for _ in range(n)]

        def add(w, nb, c):
            m = best[w][nb]
            if c < m[0]:
                m[1] = m[0]
                m[0] = c
            elif c < m[1]:
                m[1] = c

        ans = INF
        for u, v, c in edges:
            if b[u] == b[v]:
                ans = min(ans, c)
            add(u, b[v], c)
            add(v, b[u], c)

        for w in range(n):
            if b[w] == 0:
                for t in (0, 1):
                    m = best[w][t]
                    if m[1] < INF:
                        ans = min(ans, m[0] + m[1])
            else:
                a, c = best[w][0][0], best[w][1][0]
                if a < INF and c < INF:
                    ans = min(ans, a + c)

        return -1 if ans == INF else ans