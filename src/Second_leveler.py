import BufferAndSplitterInsertionSolver as BSI


class Next_delay_calculater:
    def __init__(self, module):
        self.module = module
        self.raw_delay_table = dict()

    def clear_delay(self):
        self.raw_delay_table = dict()

    def get_delay(self, node):
        if self.raw_delay_table.get(node) is not None:
            return self.raw_delay_table.get(node)
        raw_delay = 0
        for port_name, wire in node.get_inputs():
            (next_node, _next_port_name) = wire.input_port
            wire_delay = wire.output_delay[(node, port_name)]
            raw_delay = max(raw_delay, self.get_delay(next_node) + wire_delay)
        raw_delay += 1
        self.raw_delay_table[node] = raw_delay
        return raw_delay

    def get_wire_delay(self, wire, output_key):
        return self.get_delay(wire.input_port[0]) + wire.output_delay[output_key]

    def max_delay(self):
        return self.get_delay(self.module.output)


class Second_leveler:
    def __init__(self, module, wire_delay_adder):
        self.module = module
        self.delay_calculater = Next_delay_calculater(module)
        self.unprocess_wire = set()
        self.wire_delay_adder = wire_delay_adder

    def process(self):
        self.wire_sequence = list()
        self._level_up()
        self.level_outputs()

    def calculate_wire_delay(self, wire):
        for key in wire.output_delay:
            node, port_name = key
            mutual = max(self.delay_calculater.get_wire_delay(
                v, (node, k)) for k, v in node.get_inputs())
            margin = mutual - \
                self.delay_calculater.get_wire_delay(wire, (node, port_name))
            wire.output_delay[key] += margin

    def get_wire_extra_delay(self, wire):
        node_port_list = list()
        S = list()
        for key, value in wire.output_delay.items():
            node_port_list.append(key)
            S.append(value)
        solver = BSI.DP_Solver()
        res = solver.solve(S.copy(), self.module.library.max_fan_out)
        return node_port_list, res

    def _level_up(self):
        for wire in self.module.wires:
            if len(wire.output_delay) > 1:
                for key in wire.output_delay:
                    wire.output_delay[key] = 1
                self.unprocess_wire.add(wire)
        while len(self.unprocess_wire) > 0:
            self.wire_sequence = list(self.unprocess_wire)
            self.delay_calculater.clear_delay()
            self.wire_sequence.sort(
                key=lambda x: (self.delay_calculater.get_delay(x.input_port[0]), x.max_delay()))
            cur_wire = self.wire_sequence[0]
            self.unprocess_wire.remove(cur_wire)
            self.calculate_wire_delay(cur_wire)
            self.wire_delay_adder.wire_add_delay(cur_wire)

    def level_outputs(self):
        self.delay_calculater.clear_delay()
        for wire in self.module.wires:
            in_delay = self.delay_calculater.get_delay(wire.input_port[0])
            for node, port_name in wire.output_delay:
                wire.output_delay[(node, port_name)] = self.delay_calculater.get_delay(
                    node) - in_delay - 1
