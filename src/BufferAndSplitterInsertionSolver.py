class Node:
    def __init__(self, L, R, childs):
        self.L = L
        self.R = R
        self.childs = childs

    def isLeaf(self):
        return not isinstance(self.childs, list)


class DP_Solver:
    def __init__(self):
        self.INF = 999999999999999999999999

    def __dfs(self, L, R, SPO, level):
        if SPO < 1:
            return (self.INF, self.INF)
        if level > self.bufferNum[self.idList[L]]:
            return (self.INF, self.INF)
        if (L, R, SPO, level) in self.dp:
            return self.dp[(L, R, SPO, level)]
        if L == R:
            return (0, self.bufferNum[self.idList[L]] - level)
        res = (self.INF, self.INF)
        self.pivot[(L, R, SPO, level)] = None
        if SPO == 1:
            for k in range(1, self.SPO_max + 1):
                RT = self.__dfs(L, R, k, level + 1)
                (nLV, nD) = RT
                ans = (nLV, nD + 1)
                if res > ans:
                    res = ans
                    self.pivot[(L, R, SPO, level)] = (k, level + 1)
            # '''
            if res[0] == self.INF:
                for k in range(2, self.SPO_max + 1):
                    RT = self.__dfs(L, R, k, level)
                    (nLV, nD) = RT
                    ans = (nLV + 1, nD + 1)
                    if res > ans:
                        res = ans
                        self.pivot[(L, R, SPO, level)] = (k, level)
            # '''
        else:
            for p in range(L, R):
                LP = self.__dfs(L, p, SPO - 1, level)
                RP = self.__dfs(p + 1, R, 1, level)
                ans = (max(LP[0], RP[0]), LP[1]+RP[1])
                if res > ans:
                    res = ans
                    self.pivot[(L, R, SPO, level)] = (p, level)
        self.dp[(L, R, SPO, level)] = res
        return res

    def __build(self, L, R, SPO, level, rL=0, createNode=False):
        if L == R:
            res = Node(L, R, self.idList[L])
            #print(self.bufferNum[self.idList[L]], rL + (self.bufferNum[self.idList[L]] - level))
            self.bufferNum[self.idList[L]] = \
                rL + (self.bufferNum[self.idList[L]] - level)
            #print(self.bufferNum[self.idList[L]], rL + (self.bufferNum[self.idList[L]] - level))
            for i in range(self.bufferNum[self.idList[L]] - level):
                res = Node(L, R, [res])
            if createNode:
                res = Node(L, R, [res])
            return res
        if SPO == 1:
            (k, nLV) = self.pivot[(L, R, SPO, level)]
            res = self.__build(L, R, k, nLV, rL + 1, True)
            res.L = L
            res.R = R
            if createNode:
                res = Node(L, R, [res])
            return res
        (p, nLV) = self.pivot[(L, R, SPO, level)]
        res = self.__build(L, p, SPO - 1, nLV, rL, createNode)
        assert isinstance(res, Node)
        res.childs.append(self.__build(p + 1, R, 1, nLV, rL))
        res.L = L
        res.R = R
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

        while(True):
            self.dp = dict()
            self.pivot = dict()
            search_result = self.__dfs(0, N - 1, 1, 0)
            if search_result[0] != self.INF and search_result[1] != self.INF:
                break
            for i in range(len(self.bufferNum)):
                self.bufferNum[i] += 1

        assert(search_result[0] != self.INF and search_result[1] != self.INF)

        return search_result, self.__build(0, len(bufferNum) - 1, 1, 0)
