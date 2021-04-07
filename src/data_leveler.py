import random


class Delay_initialer:
    def __init__(self, module):
        self.module = module
        self.raw_delay_table = dict()

    def __getitem__(self, item):
        return self.raw_delay_table[item]

    def max_delay(self):
        return max(self.raw_delay_table.values())


class Up_delay_initialer(Delay_initialer):
    def __init__(self, module):
        super().__init__(module)
        self.create_raw_delay()

    def create_raw_delay(self):
        def dfs(node):
            if node in self.raw_delay_table:
                return self.raw_delay_table[node]
            raw_delay = 0
            for _port_name, wire in node.get_outputs():
                for next_node, next_port_name in wire.output_port_set:
                    wire_delay = wire.output_delay[(next_node, next_port_name)]
                    raw_delay = max(raw_delay, dfs(next_node) + wire_delay)
            raw_delay += 1
            self.raw_delay_table[node] = raw_delay
            return raw_delay
        self.raw_delay_table = dict()
        dfs(self.module.input)


class Down_delay_initialer(Delay_initialer):
    def __init__(self, module):
        super().__init__(module)

    def create_raw_delay(self):
        def dfs(node):
            if node in self.raw_delay_table:
                return self.raw_delay_table[node]
            raw_delay = 0
            for port_name, wire in node.get_inputs():
                (next_node, _next_port_name) = wire.input_port
                wire_delay = wire.output_delay[(node, port_name)]
                raw_delay = max(raw_delay, dfs(next_node) + wire_delay)
            raw_delay += 1
            self.raw_delay_table[node] = raw_delay
            return raw_delay
        self.raw_delay_table = dict()
        dfs(self.module.output)


class DP_delay_initialer(Delay_initialer):
    def __init__(self, module, K):
        super().__init__(module)
        self.K = K

    def get_K_Feasible_Cuts(self, node):
        BaseCut = list()
        BaseCost = 0
        for port_name, wire in node.get_inputs():
            BaseCut.append(((port_name, wire, node), 0))

        K = max(self.K, len(BaseCut))

        def normal():
            yield (BaseCut, BaseCost)
        
        if K == len(BaseCut):
            return normal()

        def dfs(Cut, idx, Cost):
            if len(Cut) > K:
                return
            if idx == len(Cut):
                yield (Cut, Cost)
                return
            yield from dfs(Cut, idx+1, Cost)
            ((cur_port_name, wire, cur_node), wire_cost) = Cut[idx]
            wire_delay = wire.output_delay[(cur_node, cur_port_name)]
            Cost += wire_delay
            wire_cost += wire_delay + 1
            (next_node, _) = wire.input_port
            if len(next_node.get_inputs()) == 0:
                return
            if len(Cut)-1+len(next_node.get_inputs()) > K:
                return
            Left = Cut[0:idx]
            Right = Cut[idx+1:]
            for next_port_name, next_wire in next_node.get_inputs():
                Left.append(
                    ((next_port_name, next_wire, next_node), wire_cost))
            Left.extend(Right)
            yield from dfs(Left, idx+1, Cost)
        return dfs(BaseCut, 0, BaseCost)

    def create_raw_delay(self):
        self.Down_delay = Down_delay_initialer(self.module)
        self.Down_delay.create_raw_delay()
        self.DP_table = dict()
        self.DP_table[self.module.input] = ([], 0)

        def dp(node):
            if node in self.DP_table:
                return self.DP_table[node]
            self.DP_table[node] = None
            for (Cut, Cost) in self.get_K_Feasible_Cuts(node):
                SLD = list()
                for i in range(len(Cut)):
                    ((port_name, wire, nd), wire_cost) = Cut[i]
                    (next_node, _next_port_name) = wire.input_port
                    wire_delay = wire.output_delay[(nd, port_name)]
                    SLD.append(self.Down_delay[next_node] + wire_cost + wire_delay)
                    Cost += dp(next_node)[1]
                SLDmax = max(SLD)
                for i in range(len(Cut)):
                    Cost += SLDmax - SLD[i]
                    Cut[i] = (Cut[i][0], SLDmax - SLD[i])
                if self.DP_table[node] is None or self.DP_table[node][1] > Cost:
                    self.DP_table[node] = (Cut, Cost)
            return self.DP_table[node]

        dp(self.module.output)

        def getCutSet(node):
            CutSet = set()
            for ((port_name, wire, nd), wire_cost) in self.DP_table[node][0]:
                CutSet.add((port_name, wire))
                wire.output_delay[(nd, port_name)] += wire_cost
            return CutSet

        self.raw_delay_table = dict()

        def dfs(node, Cut):
            if node in self.raw_delay_table:
                return self.raw_delay_table[node]
            raw_delay = 0
            for port_name, wire in node.get_inputs():
                nextCut = Cut
                (next_node, _next_port_name) = wire.input_port
                if (port_name, wire) in Cut:
                    nextCut = getCutSet(next_node)
                wire_delay = wire.output_delay[(node, port_name)]
                raw_delay = max(raw_delay, dfs(
                    next_node, nextCut) + wire_delay)
            raw_delay += 1
            self.raw_delay_table[node] = raw_delay
            return raw_delay

        dfs(self.module.output, getCutSet(self.module.output))


class Leveler:
    def __init__(self, module, delay_initialer, Type, wire_delay_adder, need_legal_delay=False):
        self.module = module
        self.delay_initialer = delay_initialer
        self.wire_delay_adder = wire_delay_adder
        self.unprocess_wire = module.wires.copy()
        self.need_legal_delay = need_legal_delay
        if Type == 'D':
            self.begin = self.module.input
            self.end = self.module.output
        elif Type == 'U':
            self.begin = self.module.output
            self.end = self.module.input
        else:
            assert(Type == 'D' or Type == 'U')

    def process(self):
        self.wire_sequence = list()
        self._level_up()

    def init_old_legal_delay(self):
        self.old_legal_delay = dict()
        for wire in self.module.wires:
            if len(wire.output_delay) > 1:
                self.wire_delay_adder.wire_add_delay(wire)
                self.old_legal_delay[wire] = wire.output_delay.copy()

    def reset_unprocess_wire_delay(self):
        for wire in self.unprocess_wire:
            if len(wire.output_delay) <= 1:
                for key in wire.output_delay:
                    wire.output_delay[key] = 0
            else:
                if self.need_legal_delay:
                    wire.output_delay = self.old_legal_delay[wire]
                else:
                    for key in wire.output_delay:
                        wire.output_delay[key] = 1

    def cal_wire_delay(self):
        self.delay_initialer.create_raw_delay()
        for wire in self.module.wires:
            input_delay = self.delay_initialer[wire.input_port[0]]
            for node, port_name in wire.output_port_set:
                output_delay = self.delay_initialer[node]
                wire.output_delay[(node, port_name)] = abs(
                    output_delay - input_delay) - 1

    def _create_wire_sequence(self):
        self.wire_sequence = list(self.unprocess_wire)
        random.shuffle(self.wire_sequence)
        self.wire_sequence.sort(
            key=lambda x: (self.delay_initialer[x.input_port[0]], x.max_delay()))
        first_node = self.wire_sequence[0].input_port[0]
        back_node = self.wire_sequence[-1].input_port[0]
        if first_node == self.end or back_node == self.begin:
            self.wire_sequence.sort(
                key=lambda x: (-self.delay_initialer[x.input_port[0]], x.max_delay()))

    def _level_up(self):
        if self.need_legal_delay:
            self.init_old_legal_delay()
        else:
            while len(self.unprocess_wire) > 0:
                self.reset_unprocess_wire_delay()
                self.cal_wire_delay()
                self._create_wire_sequence()
                wire = self.wire_sequence[0]
                self.unprocess_wire.remove(wire)
                self.wire_delay_adder.wire_add_delay(wire)
        self.cal_wire_delay()
