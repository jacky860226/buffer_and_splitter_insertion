import BufferAndSplitterInsertionSolver as BSI


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
            for port_name, wire in node.get_outputs():
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
                (next_node, next_port_name) = wire.input_port
                wire_delay = wire.output_delay[(node, port_name)]
                raw_delay = max(raw_delay, dfs(next_node) + wire_delay)
            raw_delay += 1
            self.raw_delay_table[node] = raw_delay
            return raw_delay
        self.raw_delay_table = dict()
        dfs(self.module.output)


class Leveler:
    def __init__(self, module, delay_initialer, Type):
        self.module = module
        self.delay_initialer = delay_initialer
        self.unprocess_wire = module.wires.copy()
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
        self.check()

    def reset_unprocess_wire_delay(self):
        for wire in self.unprocess_wire:
            for key in wire.output_delay:
                wire.output_delay[key] = 0

    def cal_wire_delay(self):
        self.delay_initialer.create_raw_delay()
        for wire in self.module.wires:
            input_delay = self.delay_initialer[wire.input_port[0]]
            for node, port_name in wire.output_port_set:
                output_delay = self.delay_initialer[node]
                wire.output_delay[(node, port_name)] = abs(
                    output_delay - input_delay) - 1

    def get_wire_extra_delay(self, wire):
        S = list(wire.output_delay.values())
        solver = BSI.DP_Solver()
        res = solver.solve(S, self.module.library.max_fan_out)
        return res

    def _create_wire_sequence(self):
        self.wire_sequence = list()
        node_list = list(self.module.cell_dict.values())
        node_list.append(self.module.input)
        node_list.append(self.module.output)
        node_list.sort(key=lambda x: self.delay_initialer[x])
        if node_list[0] == self.end:
            node_list.sort(key=lambda x: -self.delay_initialer[x])
        assert(node_list[0] == self.begin)
        for node in node_list:
            for port_name, wire in node.get_outputs():
                if wire in self.unprocess_wire:
                    self.wire_sequence.append(wire)

    def _level_up(self):
        while True:
            self.reset_unprocess_wire_delay()
            self.cal_wire_delay()
            self._create_wire_sequence()
            if len(self.wire_sequence) == 0:
                break
            wire = self.wire_sequence[0]
            extra_delay = self.get_wire_extra_delay(wire)[0][1]
            for key in wire.output_delay:
                wire.output_delay[key] += extra_delay
            self.unprocess_wire.remove(wire)
        self.cal_wire_delay()

    def check(self):
        ans = 0
        for w in self.module.wires:
            res = self.get_wire_extra_delay(w)
            assert(res[0][1] == 0)
            ans += res[0][0]
        return ans
