import BufferAndSplitterInsertionSolver as BSI
from data_leveler import Up_delay_initialer
import random

class DynamicProgrammingBase:
    def __init__(self, module, solverTy):
        self.module = module
        self.solverTy = solverTy
        self.delays = Up_delay_initialer(module)

    def get_wire_extra_delay(self, wire):
        node_port_list = list()
        S = list()
        other = list()
        itemList = list(wire.output_delay.items())
        random.shuffle(itemList)
        for key, value in itemList:
            node_port_list.append(key)
            S.append(value)
            if key[0] in self.delays.raw_delay_table:
                other.append(-self.delays[key[0]])
            else:
                other.append(0)
        solver = self.solverTy()
        res = solver.solve(S.copy(), self.module.library.max_fan_out, other)
        return node_port_list, res

    def wire_add_delay(self, wire):
        node_port_list, res = self.get_wire_extra_delay(wire)
        new_delay = res[0][1]
        for i in range(len(node_port_list)):
            key = node_port_list[i]
            wire.output_delay[key] = new_delay[i]


class DynamicProgramming(DynamicProgrammingBase):
    def __init__(self, module):
        super().__init__(module, BSI.DP_Solver)


class DynamicProgramming2(DynamicProgrammingBase):
    def __init__(self, module):
        super().__init__(module, BSI.DP_Solver_2)


class PsudoNode:
    def __init__(self, child, delta, parent=None):
        self.child = child
        self.delta = delta
        self.parent = parent

    def sort_child(self):
        def cmp(x):
            if isinstance(x, PsudoNode):
                return x.delta
            else:
                return x[2]
        self.child.sort(key=cmp)

    def add_parent(self):
        assert(self.parent == None)
        self.parent = PsudoNode([self], 0)
        for i in range(len(self.child)):
            w = self.child[i]
            if isinstance(w, PsudoNode):
                if w.delta > 0:
                    w.delta -= 1
            else:
                if w[2] > 0:
                    self.child[i] = (w[0], w[1], w[2] - 1)

    def pull(self):
        min_delta = 999999999999999999999999999
        for w in self.child:
            if isinstance(w, PsudoNode):
                min_delta = min(min_delta, w.delta)
            else:
                min_delta = min(min_delta, w[2])
        assert(min_delta < 999999999999999999999999999)
        for i in range(len(self.child)):
            w = self.child[i]
            if isinstance(w, PsudoNode):
                w.delta -= min_delta
            else:
                self.child[i] = (w[0], w[1], w[2] - min_delta)
        self.delta += min_delta

    def dfs(self):
        self.sort_child()
        res = [(i[0], i[1], i[2]-1)
               for i in self.child if i[2] != self.child[0][2]]
        if len(res) <= 1:
            return self
        self.child = [i for i in self.child if i[2] == self.child[0][2]]
        self.child.append(PsudoNode(res, 0, self))
        return self.child[-1]


class SecondAdder:
    def __init__(self, module):
        self.module = module

    def _decompose(self, total):
        degree = self.module.library.max_fan_out
        basket = list()
        while total > degree:
            basket.append(degree)
            total = total - degree
        if total != 0:
            basket.append(total)
        if len(basket) > 1:
            if basket[-1] == 1:
                basket[-2] = basket[-2] - 1
        del basket[-1]
        return basket

    def dfs(self, node):
        if len(node.child) <= self.module.library.max_fan_out:
            node.pull()
            if node.parent is None:
                return node
            return self.dfs(node.parent)
        if node.parent is None:
            node.add_parent()
            return self.dfs(node)
        node.sort_child()
        basket = self._decompose(len(node.child))
        for item in basket:
            res = []
            for i in range(item):
                res.append(node.child.pop())
            new_node = PsudoNode(res, 0, node.parent)
            new_node.pull()
            node.parent.child.append(new_node)
        node.pull()
        return self.dfs(node.parent)

    def delay_assign(self, wire, node, deep=0):
        if not isinstance(node, PsudoNode):
            wire.output_delay[(node[0], node[1])] = node[2] + deep
            return
        deep += 1 + node.delta
        for ch in node.child:
            self.delay_assign(wire, ch, deep)

    def wire_add_delay(self, wire):
        S = list()
        if len(wire.output_delay) <= 1:
            return
        for key, value in wire.output_delay.items():
            S.append((key[0], key[1], max(value, 1) - 1))
        root = PsudoNode(S, 0).dfs()
        root = self.dfs(root)
        self.delay_assign(wire, root)
