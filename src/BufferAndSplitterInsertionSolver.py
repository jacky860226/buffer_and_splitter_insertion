class DP_Solver:
    def __init__(self):
        self.INF = 999999999999999999999999

    def __dfs(self, L, R, SPO, level):
        if SPO < 1:
            return self.INF
        if level > self.bufferNum[self.idList[L]]:
            return self.INF
        if (L, R, SPO, level) in self.dp:
            return self.dp[(L, R, SPO, level)]
        if L == R:
            return self.bufferNum[self.idList[L]] - level
        res = self.INF
        self.pivot[(L, R, SPO, level)] = None
        if SPO == 1:
            for k in range(1, self.SPO_max + 1):
                ans = self.__dfs(L, R, k, level + 1) + 1
                if res > ans:
                    res = ans
                    self.pivot[(L, R, SPO, level)] = k
        else:
            for p in range(L, R):
                ans = self.__dfs(L, p, SPO - 1, level) + \
                    self.__dfs(p + 1, R, 1, level)
                if res > ans:
                    res = ans
                    self.pivot[(L, R, SPO, level)] = p
        self.dp[(L, R, SPO, level)] = res
        return res

    def __build(self, L, R, SPO, level, realLevel=0, createNode=False):
        if L == R:
            res = self.idList[L]
            buffer_delay = self.bufferNum[res] - level
            self.bufferNum[res] = realLevel + buffer_delay
            for i in range(buffer_delay):
                res = [res]
            if createNode:
                res = [res]
            return res
        if SPO == 1:
            k = self.pivot[(L, R, SPO, level)]
            res = self.__build(L, R, k, level + 1, realLevel + 1, True)
            if createNode:
                res = [res]
            return res
        p = self.pivot[(L, R, SPO, level)]
        res = self.__build(L, p, SPO - 1, level, realLevel, createNode)
        assert isinstance(res, list)
        res.append(self.__build(p + 1, R, 1, level, realLevel))
        return res

    def solve(self, bufferNum, SPO_max):
        for num in bufferNum:
            if num < 0:
                return None

        N = len(bufferNum)
        self.bufferNum = bufferNum
        self.idList = [i for i in range(N)]
        self.idList.sort(key=lambda x: self.bufferNum[x])
        self.SPO_max = SPO_max

        search_result = None
        while True:
            self.dp = dict()
            self.pivot = dict()
            search_result = self.__dfs(0, N - 1, 1, 0)
            if search_result < self.INF:
                break
            for i in range(N):
                self.bufferNum[i] += 1

        tree = self.__build(0, len(bufferNum) - 1, 1, 0)

        return (search_result, self.bufferNum), tree
