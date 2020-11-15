import math
class DP_Solver:
    def __init__(self):
        self.INF = 999999999999999999999999

    def __dfs(self, L, R, SPO, level):
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

    def solve(self, bufferNum, SPO_max, other=None):
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


class DP_Solver_2:
    def __init__(self):
        self.INF = 999999999999999999999999

    def __dfs(self, L, R, SPO, level):
        if level > self.N + self.bufferNum[self.idList[L]]:
            return (self.INF, self.INF)
        if (L, R, SPO, level) in self.dp:
            return self.dp[(L, R, SPO, level)]
        if L == R:
            if level > self.bufferNum[self.idList[L]]:
                return level - self.bufferNum[self.idList[L]], 0
            return 0, self.bufferNum[self.idList[L]] - level
        res = (self.INF, self.INF)
        self.pivot[(L, R, SPO, level)] = None
        if SPO == 1:
            for k in range(1, self.SPO_max + 1):
                out = self.__dfs(L, R, k, level + 1)
                ans = (out[0], out[1] + 1)
                if res > ans:
                    res = ans
                    self.pivot[(L, R, SPO, level)] = (k, level + 1)
        else:
            for p in range(L, R):
                first = self.__dfs(L, p, SPO - 1, level)
                second = self.__dfs(p + 1, R, 1, level)
                ans = (first[0] + second[0], first[1] + second[1])
                if res > ans:
                    res = ans
                    self.pivot[(L, R, SPO, level)] = (p, level)
        self.dp[(L, R, SPO, level)] = res
        return res

    def __build(self, L, R, SPO, level, realLevel=0, createNode=False):
        if L == R:
            res = self.idList[L]
            buffer_delay = max(self.bufferNum[res] - level, 0)
            self.bufferNum[res] = realLevel + buffer_delay
            for i in range(buffer_delay):
                res = [res]
            if createNode:
                res = [res]
            return res
        if SPO == 1:
            k, next_level = self.pivot[(L, R, SPO, level)]
            res = self.__build(L, R, k, next_level, realLevel + 1, True)
            if createNode:
                res = [res]
            return res
        p, next_level = self.pivot[(L, R, SPO, level)]
        res = self.__build(L, p, SPO - 1, next_level, realLevel, createNode)
        assert isinstance(res, list)
        res.append(self.__build(p + 1, R, 1, next_level, realLevel))
        return res

    def solve(self, bufferNum, SPO_max, other=None):
        for num in bufferNum:
            if num < 0:
                return None

        N = len(bufferNum)
        self.bufferNum = bufferNum
        self.idList = [i for i in range(N)]
        if other is not None:
            self.idList.sort(key=lambda x: (self.bufferNum[x], other[x]))
        else:
            self.idList.sort(key=lambda x: self.bufferNum[x])
        self.SPO_max = SPO_max

        self.N = int(math.log2(N)/2) + 1

        search_result = None
        self.dp = dict()
        self.pivot = dict()
        search_result = self.__dfs(0, N - 1, 1, 0)
        assert(search_result[0] < self.INF and search_result[1] < self.INF)

        tree = self.__build(0, len(bufferNum) - 1, 1, 0)

        return (search_result, self.bufferNum), tree
